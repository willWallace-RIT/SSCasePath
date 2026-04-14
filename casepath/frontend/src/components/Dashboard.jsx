import React, { useEffect, useState } from "react";
import { getCases } from "../api";

export default function Dashboard() {
  const [cases, setCases] = useState([]);

  useEffect(() => {
    getCases().then(setCases);
  }, []);

  return (
    <div>
      <h2>Cases</h2>

      {cases.map((c) => (
        <div key={c.case_id} style={{ border: "1px solid #ccc", margin: 10 }}>
          <h3>{c.case_id}</h3>
          <p>Classification: {c.classification}</p>
          <p>Cost: ${c.estimated_cost}</p>
          <p>Services: {c.recommended_services?.join(", ")}</p>
        </div>
      ))}
    </div>
  );
}
