import React from "react";

/**
 * ResultView - present the structured JSON result in a polished layout
 * Props:
 *   - result: { claim, verdict, confidence, summary, sources, timeline, provenance, notes }
 */
export default function ResultView({ result }) {
  const { claim, verdict, confidence, summary, sources = [], timeline = [], provenance = [], notes } = result;

  function verdictColor(verdict) {
    const v = (verdict || "").toLowerCase();
    if (v.includes("likely true") || v.includes("true")) return "#046c4e"; // green
    if (v.includes("false") || v.includes("likely false")) return "#b91c1c"; // red
    return "#b7791f"; // amber for mixed
  }

  return (
    <div className="result-card">
      <div className="result-header">
        <div>
          <div className="claim-title">Claim</div>
          <div className="claim-text">{claim}</div>
        </div>

        <div className="verdict-area">
          <div className="verdict-badge" style={{ background: verdictColor(verdict) }}>
            {verdict}
          </div>
          <div className="confidence">
            <div className="confidence-label">Confidence</div>
            <div className="confidence-bar">
              <div className="confidence-fill" style={{ width: `${confidence}%` }} />
            </div>
            <div className="confidence-num">{confidence}%</div>
          </div>
        </div>
      </div>

      <div className="summary">{summary}</div>

      <div className="section">
        <h3>Sources</h3>
        <div className="sources-grid">
          {sources.map((s) => (
            <div className="source-card" key={s.id}>
              <div className="source-title">{s.title}</div>
              <div className="source-meta">
                <span>{s.date || "—"}</span>
                <span>•</span>
                <span>Reliability: {Math.round((s.reliability || 0) * 100)}%</span>
              </div>
              <div className="source-snippet">"{s.snippet}"</div>
              <div className="source-actions">
                <a href={s.url} target="_blank" rel="noreferrer">Open</a>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="two-columns">
        <div className="section">
          <h3>Timeline</h3>
          {timeline.length === 0 ? <div className="muted">No timeline available</div> : (
            <ol className="timeline-list">
              {timeline.map((t, i) => (
                <li key={i}><span className="tl-date">{t.date}</span> — {t.event}</li>
              ))}
            </ol>
          )}
        </div>

        <div className="section">
          <h3>Provenance (quotes)</h3>
          {provenance.length === 0 ? <div className="muted">No provenance available</div> : (
            <ul className="prov-list">
              {provenance.map((p, i) => (
                <li key={i}>
                  <div className="prov-quote">“{p.quote}”</div>
                  <div className="prov-meta">Source: {p.source} {p.loc ? `• ${p.loc}` : ""}</div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>

      {notes && <div className="notes-box">{notes}</div>}
    </div>
  );
}
