import React, { useState } from "react";
import axios from "axios";
import ResultView from "./ResultView";
import "./index.css";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function analyze() {
    setError("");
    setLoading(true);
    setResult(null);
    try {
      const res = await axios.post("http://localhost:8000/api/analyze", { text });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setError(
        err?.response?.data?.detail || err.message || "Unable to reach backend"
      );
    } finally {
      setLoading(false);
    }
  }

  function loadSample() {
    const sample = "Eating carrots improves night vision.";
    setText(sample);
    setResult(null);
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>TruthTracer Pro</h1>
        <div className="header-sub">RAG demo — mock backend (resume-ready UI)</div>
      </header>

      <main className="container">
        <section className="left-panel">
          <label className="label">Claim / Text</label>
          <textarea
            className="input"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste a claim, short article text, or URL (demo)"
          />

          <div className="controls">
            <button className="btn primary" onClick={analyze} disabled={loading}>
              {loading ? "Analyzing..." : "Analyze"}
            </button>
            <button className="btn" onClick={loadSample}>
              Load sample
            </button>
            <button
              className="btn"
              onClick={() => {
                setText("");
                setResult(null);
                setError("");
              }}
            >
              Clear
            </button>
          </div>

          {error && <div className="error-box">{error}</div>}

          <div className="notes">
            <strong>Notes:</strong> This demo uses a mock RAG backend. Toggle to real model in the backend with <code>USE_REAL_MODEL=true</code>.
          </div>
        </section>

        <section className="right-panel">
          {result ? (
            <ResultView result={result} />
          ) : (
            <div className="empty-state">
              <p>No result yet. Paste a claim and click <b>Analyze</b>.</p>
              <p>Try: <i>Eating carrots improves night vision.</i></p>
            </div>
          )}
        </section>
      </main>

      <footer className="footer">
        <div>TruthTracer Pro — Demo • Resume-ready UI</div>
      </footer>
    </div>
  );
}
