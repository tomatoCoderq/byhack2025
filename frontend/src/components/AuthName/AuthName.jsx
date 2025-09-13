import React, { useState, useEffect, useRef } from 'react'
import Button from '../Button/Button'

export default function AuthName({ onSubmit, onCancel, t, lang }) {
  const [name, setName] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const inputRef = useRef(null)

  useEffect(() => { inputRef.current?.focus() }, [])

  const handleSubmit = async (e) => {
    e?.preventDefault?.()
    const n = name.trim()
    if (!n  || loading) return
    setError('')
    setLoading(true)
    try {
      // Try login first; if user doesn't exist, register and proceed
      let res = await fetch('http://localhost:8000/users/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: n })
      })
      if (!res.ok) {
        // Fallback to register
        res = await fetch('http://localhost:8000/users/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name: n })
        })
      }
      if (!res.ok) throw new Error('Auth request failed')
      const data = await res.json().catch(() => ({}))
      const userId = data?.id ?? data?.userId ?? data?.user_id
      if (userId !== undefined && userId !== null) {
        try { localStorage.setItem('userId', String(userId)) } catch {}
      } else {
        throw new Error('Missing user id in response')
      }
      onSubmit?.(n)
    } catch (err) {
      console.error(err)
      setError(t?.loginError  (lang === 'tt' ? 'Керү хатасы. Яңадан сынап карагыз.' : 'Не удалось войти. Попробуйте ещё раз.'))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="overlay" onClick={onCancel}>
      <section className="auth" onClick={(e) => e.stopPropagation()} role="dialog" aria-modal="true">
        <h3 className="auth__title">{lang === 'tt' ? 'Исемеңне керт' : 'Введите имя'}</h3>
        <form className="auth__form" onSubmit={handleSubmit}>
          <input
            ref={inputRef}
            className="auth__input"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder={lang === 'tt' ? 'Исемеңне керт' : 'Введите имя'}
          />
          {error ? (
            <div style={{ color: '#b00020', fontSize: 14 }}>{error}</div>
          ) : null}
          <div className="auth__actions">
            <Button type="submit" side="left" disabled={loading}>{lang === 'tt' ? 'Керү' : 'Войти'}</Button>
            <Button type="button" side="right" onClick={onCancel}>{lang === 'tt' ? 'Артка' : 'Назад'}</Button>
          </div>
        </form>
      </section>
    </div>
  )
}