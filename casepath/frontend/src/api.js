const API = "http://localhost:8000";

export async function createCase(caseData) {
  const res = await fetch(`${API}/case`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(caseData),
  });

  return res.json();
}

export async function getCases() {
  const res = await fetch(`${API}/cases`);
  return res.json();
}
