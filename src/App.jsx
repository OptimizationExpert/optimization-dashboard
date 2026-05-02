import { useEffect, useState } from "react";

export default function App() {
  const [items, setItems] = useState([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    fetch("/optimization-dashboard/data/items.json")
      .then(res => res.json())
      .then(data => {
        setItems(data.items || []);
      })
      .catch(err => {
        console.error("Failed to load data", err);
      });
  }, []);

  const filtered = items.filter(item =>
    item.title.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div style={{ padding: 24, fontFamily: "system-ui" }}>
      <h1>Optimization Research Dashboard</h1>

      <input
        placeholder="Search MILP, CP, Optimization…"
        style={{ margin: "16px 0", padding: 8, width: "100%" }}
        value={query}
        onChange={e => setQuery(e.target.value)}
      />

      <ul>
        {filtered.map((item, idx) => (
          <li key={idx} style={{ marginBottom: 12 }}>
            <strong>{item.title}</strong>
            <br />
            <small>
              {item.source} · {item.published}
            </small>
            <br />
            <a href={item.url} target="_blank">Open</a>
          </li>
        ))}
      </ul>
    </div>
  );
}