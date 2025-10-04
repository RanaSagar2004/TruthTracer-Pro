import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './index.css';

const rootEl = document.getElementById('root');
if (!rootEl) {
  throw new Error('No root element found (expected <div id="root"></div> in public/index.html)');
}
createRoot(rootEl).render(<App />);
