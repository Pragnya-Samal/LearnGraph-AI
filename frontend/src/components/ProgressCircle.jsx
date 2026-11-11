export default function ProgressCircle({
  percentage = 0,
  size = 140,
  strokeWidth = 10,
  label = 'Knowledge',
  color = 'var(--primary)',
  className = '',
}) {
  const safePercent = Math.min(100, Math.max(0, Math.round(percentage)));
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (safePercent / 100) * circumference;

  return (
    <div className={`progress-circle-container ${className}`.trim()} style={{ width: size, height: size }}>
      <svg width={size} height={size} className="progress-circle-svg">
        <circle
          className="progress-circle-bg"
          cx={size / 2}
          cy={size / 2}
          r={radius}
          strokeWidth={strokeWidth}
        />
        <circle
          className="progress-circle-bar"
          cx={size / 2}
          cy={size / 2}
          r={radius}
          strokeWidth={strokeWidth}
          stroke={color}
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
        />
      </svg>
      <div className="progress-circle-content">
        <span className="progress-circle-percent">{safePercent}%</span>
        {label && <span className="progress-circle-sublabel">{label}</span>}
      </div>
    </div>
  );
}
