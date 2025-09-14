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

export async function createStoryAndDialogue({
  userId,
  personaName,
  context = '',
  style = null,
  persona = null,
} = {}) {
  const payload = {
    user_id: userId,
    persona_name: personaName ?? null,
    context,
    style,
    persona,
  }
  const res = await fetch(`${API_BASE}/stories`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'omit',
    mode: 'cors',
  })
  if (!res.ok) throw new Error(`Failed to create story: ${res.status}`)
  return res.json()
}

export { API_BASE }
