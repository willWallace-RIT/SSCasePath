import React, { useState } from "react";
import CaseWizard from "./components/CaseWizard";
import Dashboard from "./components/Dashboard";

export default function App() {
  const [view, setView] = useState("dashboard");

  return (
    <div style={{ padding: 20 }}>
      <h1>CasePath</h1>

      <button onClick={() => setView("dashboard")}>Dashboard</button>
      <button onClick={() => setView("wizard")}>New Case</button>

      {view === "dashboard" && <Dashboard />}
      {view === "wizard" && <CaseWizard />}
    </div>
  );
}
