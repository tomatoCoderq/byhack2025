import React, { useState, useEffect, useRef } from 'react'
import Button from '../Button/Button'

export default function AuthName({ onSubmit, onCancel, t, lang }) {
  const [name, setName] = useState('')
  const inputRef = useRef(null)

  useEffect(() => { inputRef.current?.focus() }, [])

  const handleSubmit = (e) => {
    e?.preventDefault?.()
    const n = name.trim()
    if (!n) return
    onSubmit?.(n)
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
            placeholder={lang === 'tt' ? 'Сезнең исем' : 'Ваше имя'}
          />
          <div className="auth__actions">
            <Button type="submit" side="left">{lang === 'tt' ? 'Дәвам итү' : 'Продолжить'}</Button>
            <Button type="button" side="right" onClick={onCancel}>{t?.back || 'Назад'}</Button>
          </div>
        </form>
      </section>
    </div>
  )
}

