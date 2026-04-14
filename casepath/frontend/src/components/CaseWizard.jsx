import React, { useState } from "react";
import { createCase } from "../api";

export default function CaseWizard() {
  const [form, setForm] = useState({
    case_id: "",
    client_profile: {
      age: 0,
      employment_status: "",
      housing_status: "",
      mental_health_risk: false
    }
  });

  const submit = async () => {
    const res = await createCase(form);
    alert(JSON.stringify(res, null, 2));
  };

  return (
    <div>
      <h2>New Case</h2>

      <input
        placeholder="Case ID"
        onChange={(e) => setForm({ ...form, case_id: e.target.value })}
      />

      <input
        placeholder="Age"
        type="number"
        onChange={(e) =>
          setForm({
            ...form,
            client_profile: { ...form.client_profile, age: Number(e.target.value) }
          })
        }
      />

      <input
        placeholder="Employment (employed/unemployed)"
        onChange={(e) =>
          setForm({
            ...form,
            client_profile: {
              ...form.client_profile,
              employment_status: e.target.value
            }
          })
        }
      />

      <input
        placeholder="Housing (stable/homeless)"
        onChange={(e) =>
          setForm({
            ...form,
            client_profile: {
              ...form.client_profile,
              housing_status: e.target.value
            }
          })
        }
      />

      <label>
        Mental Health Risk
        <input
          type="checkbox"
          onChange={(e) =>
            setForm({
              ...form,
              client_profile: {
                ...form.client_profile,
                mental_health_risk: e.target.checked
              }
            })
          }
        />
      </label>

      <button onClick={submit}>Submit Case</button>
    </div>
  );
}
