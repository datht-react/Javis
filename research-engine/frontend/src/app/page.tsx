"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<{ answer: string; sources: any[] } | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query, model_provider: "openrouter" }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Search failed:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 bg-slate-50 text-slate-900">
      <div className="w-full max-w-2xl space-y-8">
        <h1 className="text-4xl font-bold text-center">Javis Search</h1>
        <form onSubmit={handleSearch} className="relative">
          <input
            type="text"
            className="w-full p-4 pr-12 rounded-xl border border-slate-300 shadow-sm focus:ring-2 focus:ring-blue-500 focus:outline-none"
            placeholder="Ask anything about AI research..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            type="submit"
            disabled={loading}
            className="absolute right-3 top-3 bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 disabled:bg-slate-400"
          >
            {loading ? "..." : "→"}
          </button>
        </form>

        {result && (
          <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm space-y-4">
            <h2 className="text-xl font-semibold">Answer</h2>
            <div className="prose prose-slate max-w-none">
              <p className="whitespace-pre-wrap">{result.answer}</p>
            </div>
            <div className="pt-4 border-t border-slate-100">
              <h3 className="text-sm font-medium text-slate-500 mb-2">Sources</h3>
              <div className="flex gap-2">
                {result.sources.map((s, i) => (
                  <a
                    key={i}
                    href={s.url}
                    className="text-xs bg-slate-100 px-3 py-1 rounded-full text-blue-600 hover:underline"
                    target="_blank"
                  >
                    {s.title}
                  </a>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
