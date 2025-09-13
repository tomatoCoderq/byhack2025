const API_BASE = import.meta.env?.VITE_API_BASE || 'http://localhost:8000'

export async function fetchItems() {
  const res = await fetch(`${API_BASE}/characters`, {
    headers: { Accept: 'application/json' },
    credentials: 'omit',
    mode: 'cors',
  })
  if (!res.ok) throw new Error(`Failed to load characters: ${res.status}`)
  const data = await res.json()
  return (data || []).map((c) => ({
    id: c.id,
    title: c.title,
    image: c.image || '',
    details: c.details || {
      history: { ru: '', tt: '' },
      habitat: { ru: '', tt: '' },
      features: { ru: '', tt: '' },
    },
  }))
}

export { API_BASE }

