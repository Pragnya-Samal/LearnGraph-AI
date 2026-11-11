import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLearning } from '../contexts/LearningContext';
import Card, { CardHeader, CardTitle, CardBody } from '../components/Card';
import Button from '../components/Button';
import DonutChart from '../components/DonutChart';
import { SUBJECTS } from '../data/mockData';
import {
  ArrowRightIcon,
  FilterIcon,
} from '../components/Icons';

const CONCEPT_GRAPH = {
  'Arrays':              { subject: 'Data Structures', prerequisites: [], x: 400, y: 70,  description: 'Fundamental linear data structure storing elements in contiguous memory with O(1) index access.' },
  'Linked Lists':        { subject: 'Data Structures', prerequisites: ['Arrays'], x: 220, y: 180, description: 'Dynamic data structure with nodes connected sequentially via pointers.' },
  'Sorting':             { subject: 'Algorithms',      prerequisites: ['Arrays'], x: 580, y: 180, description: 'Systematic algorithms for arranging elements (QuickSort, MergeSort, HeapSort).' },
  'Trees':               { subject: 'Data Structures', prerequisites: ['Arrays', 'Linked Lists'], x: 140, y: 320, description: 'Hierarchical structure with parent and child nodes; foundational for BST and heaps.' },
  'Graphs':              { subject: 'Data Structures', prerequisites: ['Arrays', 'Linked Lists'], x: 300, y: 320, description: 'Non-linear data structure with vertices connected by edges.' },
  'Searching':           { subject: 'Algorithms',      prerequisites: ['Arrays', 'Sorting'], x: 500, y: 320, description: 'Methods for locating target elements (Linear Search, Binary Search).' },
  'Dynamic Programming': { subject: 'Algorithms',      prerequisites: ['Sorting', 'Searching'], x: 660, y: 320, description: 'Algorithm technique solving complex problems by breaking into overlapping subproblems.' },
  'Inheritance':         { subject: 'OOPS',            prerequisites: [], x: 200, y: 430, description: 'Derived classes inherit methods and fields from base classes.' },
  'Encapsulation':       { subject: 'OOPS',            prerequisites: [], x: 380, y: 430, description: 'Bundling state and methods within a class while restricting direct external access.' },
  'Polymorphism':        { subject: 'OOPS',            prerequisites: ['Inheritance'], x: 560, y: 430, description: 'Ability of entities to take multiple forms through method overriding and overloading.' },
};

export default function KnowledgeMap() {
  const navigate = useNavigate();
  const { conceptMap, getDonutData } = useLearning();
  const [selectedFilter, setSelectedFilter] = useState('all');
  const [selectedNode, setSelectedNode] = useState('Arrays');
  const [donutSubject, setDonutSubject] = useState('');

  const nodeInfo = Object.fromEntries(
    Object.entries(CONCEPT_GRAPH).map(([name, staticData]) => {
      const s = conceptMap[name] || { status: 'Not Assessed', score: 0, count: 0 };
      return [name, { ...staticData, knowledge: s.score, status: s.status, count: s.count || 0 }];
    })
  );

  const getNodeColor = (status) => {
    switch (status) {
      case 'Strong':       return 'var(--status-success)';
      case 'Uncertain':    return 'var(--primary)';
      case 'Weak':         return 'var(--status-warning)';
      default:             return 'var(--text-muted)';
    }
  };

  const filteredNodes = Object.entries(nodeInfo).filter(([_, info]) => {
    if (selectedFilter === 'all') return true;
    return info.status.toLowerCase().replace(' ', '-') === selectedFilter;
  });

  const currentNode = selectedNode ? nodeInfo[selectedNode] : null;

  return (
    <div className="knowledge-map-page">
      <div className="container">
        <div className="page-header">
          <h1>Interactive Knowledge Map</h1>
          <p>Visualize concept dependencies, prerequisite relationships, and your personal mastery levels.</p>
        </div>

        <div className="knowledge-map-container">
          <Card>
            <CardBody>
              <div className="filters-group">
                <span style={{ fontSize: '0.875rem', fontWeight: '600', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '0.5rem', marginRight: '0.5rem' }}>
                  <FilterIcon size={16} /> Filter:
                </span>
                {['all', 'strong', 'uncertain', 'weak', 'not-assessed'].map((f) => (
                  <button key={f} className={`filter-btn ${selectedFilter === f ? 'active' : ''}`} onClick={() => setSelectedFilter(f)}>
                    {f === 'all' ? 'All Concepts' : f.replace('-', ' ').replace(/\b\w/g, c => c.toUpperCase())}
                  </button>
                ))}
              </div>
            </CardBody>
          </Card>

          <Card>
            <CardHeader>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 'var(--space-3)' }}>
                <CardTitle>Knowledge Progress</CardTitle>
                <select
                  value={donutSubject}
                  onChange={(e) => setDonutSubject(e.target.value)}
                  className="form-select"
                  style={{ width: 'auto', minWidth: '180px', fontSize: '0.875rem' }}
                >
                  <option value="">All Subjects</option>
                  {SUBJECTS.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}
                </select>
              </div>
            </CardHeader>
            <CardBody>
              <DonutChart
                data={getDonutData(donutSubject)}
                title={donutSubject ? `${donutSubject} Learning Progress` : 'Overall Learning Progress'}
                centerLabel="Mastered"
              />
            </CardBody>
          </Card>

          {currentNode && selectedNode && (
            <Card className="animate-fade-in" style={{ borderLeft: `4px solid ${getNodeColor(currentNode.status)}` }}>
              <CardHeader>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
                  <div>
                    <span className="badge badge-neutral" style={{ marginBottom: '0.25rem' }}>{currentNode.subject}</span>
                    <CardTitle>{selectedNode}</CardTitle>
                  </div>
                  <span className="badge" style={{ backgroundColor: 'var(--bg-surface-subtle)', color: getNodeColor(currentNode.status), border: `1px solid ${getNodeColor(currentNode.status)}` }}>
                    {currentNode.status}{currentNode.knowledge > 0 ? ` · ${currentNode.knowledge}%` : ''}
                  </span>
                </div>
              </CardHeader>
              <CardBody>
                <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: 'var(--space-4)' }}>{currentNode.description}</p>
                {currentNode.prerequisites.length > 0 && (
                  <div style={{ marginBottom: 'var(--space-5)' }}>
                    <span style={{ fontSize: '0.8125rem', fontWeight: '600', color: 'var(--text-muted)' }}>PREREQUISITES:</span>
                    <div className="prereq-list">
                      {currentNode.prerequisites.map((prereq) => (
                        <span key={prereq} className="prereq-badge" style={{ borderColor: getNodeColor(nodeInfo[prereq]?.status || 'Not Assessed') }}>{prereq}</span>
                      ))}
                    </div>
                  </div>
                )}
                {currentNode.count > 0 && (
                  <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', marginBottom: 'var(--space-4)' }}>
                    Assessed {currentNode.count} time{currentNode.count > 1 ? 's' : ''} · Avg score: {currentNode.knowledge}%
                  </p>
                )}
                <Button variant="primary" onClick={() => navigate('/assessment', { state: { subject: currentNode.subject, topic: selectedNode } })}>
                  <span>Assess {selectedNode} Knowledge</span>
                  <ArrowRightIcon size={16} />
                </Button>
              </CardBody>
            </Card>
          )}

          <Card>
            <CardHeader><CardTitle>Curriculum Concepts ({filteredNodes.length})</CardTitle></CardHeader>
            <CardBody>
              <div className="nodes-grid">
                {filteredNodes.map(([nodeName, info]) => {
                  const nodeColor = getNodeColor(info.status);
                  return (
                    <div key={nodeName} className={`node-card ${selectedNode === nodeName ? 'selected' : ''}`} onClick={() => setSelectedNode(nodeName)} style={{ borderLeftColor: nodeColor }}>
                      <div className="node-header">
                        <h4>{nodeName}</h4>
                        <span className="node-status" style={{ color: nodeColor }}>{info.status}</span>
                      </div>
                      <div className="node-progress">
                        <div className="progress-bar-small">
                          <div className="progress-fill-small" style={{ width: `${info.knowledge}%`, backgroundColor: nodeColor }}></div>
                        </div>
                        <span className="progress-text">{info.knowledge > 0 ? `${info.knowledge}%` : '—'}</span>
                      </div>
                      <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', margin: 0 }}>{info.subject}</p>
                    </div>
                  );
                })}
              </div>
            </CardBody>
          </Card>
        </div>
      </div>
    </div>
  );
}
