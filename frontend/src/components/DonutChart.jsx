import { useState } from 'react';

const R = 80;       // outer radius
const IR = 50;      // inner radius (donut hole)
const CX = 110;     // center x (extra space for legend)
const CY = 100;     // center y
const SIZE_W = 340;
const SIZE_H = 200;

function polarToXY(cx, cy, r, angleDeg) {
  const rad = ((angleDeg - 90) * Math.PI) / 180;
  return { x: cx + r * Math.cos(rad), y: cy + r * Math.sin(rad) };
}

function buildArc(cx, cy, r, ir, startDeg, endDeg) {
  const gap = 1.5; // degrees gap between slices
  const s = startDeg + gap / 2;
  const e = endDeg - gap / 2;
  if (e - s <= 0) return '';
  const large = e - s > 180 ? 1 : 0;
  const o1 = polarToXY(cx, cy, r, s);
  const o2 = polarToXY(cx, cy, r, e);
  const i1 = polarToXY(cx, cy, ir, e);
  const i2 = polarToXY(cx, cy, ir, s);
  return `M ${o1.x} ${o1.y} A ${r} ${r} 0 ${large} 1 ${o2.x} ${o2.y} L ${i1.x} ${i1.y} A ${ir} ${ir} 0 ${large} 0 ${i2.x} ${i2.y} Z`;
}

export default function DonutChart({ data, title, centerLabel }) {
  const [hovered, setHovered] = useState(null);

  const total = data.reduce((s, d) => s + d.count, 0) || 1;
  const masteredPct = data.find(d => d.label === 'Mastered')?.pct ?? 0;

  // Build slices
  let cursor = 0;
  const slices = data.map((d) => {
    const sweep = (d.count / total) * 360;
    const start = cursor;
    cursor += sweep;
    return { ...d, start, end: cursor, sweep };
  });

  const activeSlice = hovered !== null ? slices[hovered] : null;

  return (
    <div className="donut-chart-wrapper">
      {title && <p className="donut-chart-title">{title}</p>}
      <div className="donut-chart-inner">
        <svg
          viewBox={`0 0 ${SIZE_W} ${SIZE_H}`}
          className="donut-svg"
          aria-label={title || 'Donut chart'}
        >
          {/* Slices */}
          {slices.map((s, i) => {
            if (s.sweep < 0.5) return null;
            const isHovered = hovered === i;
            const path = buildArc(CX, CY, isHovered ? R + 5 : R, IR, s.start, s.end);
            return (
              <path
                key={s.label}
                d={path}
                fill={s.color}
                opacity={hovered !== null && !isHovered ? 0.45 : 1}
                style={{ cursor: 'pointer', transition: 'all 0.18s ease' }}
                onMouseEnter={() => setHovered(i)}
                onMouseLeave={() => setHovered(null)}
              />
            );
          })}

          {/* Center text */}
          <text x={CX} y={CY - 10} textAnchor="middle" className="donut-center-pct">
            {masteredPct}%
          </text>
          <text x={CX} y={CY + 10} textAnchor="middle" className="donut-center-label">
            {centerLabel || 'Mastered'}
          </text>

          {/* Tooltip */}
          {activeSlice && (
            <g>
              <rect
                x={CX + R + 14}
                y={CY - 38}
                width={108}
                height={72}
                rx="6"
                fill="var(--bg-surface)"
                stroke="var(--border-medium)"
                strokeWidth="1"
                filter="drop-shadow(0 2px 6px rgba(0,0,0,0.12))"
              />
              <rect x={CX + R + 18} y={CY - 28} width={8} height={8} rx="2" fill={activeSlice.color} />
              <text x={CX + R + 30} y={CY - 21} className="donut-tooltip-label">{activeSlice.label}</text>
              <text x={CX + R + 18} y={CY - 6}  className="donut-tooltip-val">{activeSlice.count} concept{activeSlice.count !== 1 ? 's' : ''}</text>
              <text x={CX + R + 18} y={CY + 12} className="donut-tooltip-pct">{activeSlice.pct}%</text>
            </g>
          )}

          {/* Legend */}
          {data.map((d, i) => {
            const ly = 20 + i * 22;
            const lx = SIZE_W - 118;
            return (
              <g
                key={d.label}
                style={{ cursor: 'pointer' }}
                onMouseEnter={() => setHovered(i)}
                onMouseLeave={() => setHovered(null)}
                opacity={hovered !== null && hovered !== i ? 0.45 : 1}
              >
                <rect x={lx} y={ly} width={10} height={10} rx="2" fill={d.color} />
                <text x={lx + 14} y={ly + 9} className="donut-legend-label">
                  {d.label}
                </text>
                <text x={SIZE_W - 6} y={ly + 9} textAnchor="end" className="donut-legend-pct">
                  {d.pct}%
                </text>
              </g>
            );
          })}
        </svg>
      </div>
    </div>
  );
}
