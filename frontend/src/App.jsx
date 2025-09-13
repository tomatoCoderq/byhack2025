import React, { useState, useEffect } from 'react'
import { items } from './data/items'
import Header from './components/Header/Header'
import Card from './components/Card/Card'
import Modal from './components/Modal/Modal'
import Dialogue from './components/Dialogue/Dialogue'
import AuthName from './components/AuthName/AuthName'
import About from './components/About/About'
import { i18n } from './i18n'

export default function App() {
  const [selected, setSelected] = useState(null)
  const [lang, setLang] = useState('ru')
  const [view, setView] = useState('home') 
  const [active, setActive] = useState(null)
  const [userName, setUserName] = useState(null)
  const [needName, setNeedName] = useState(false)

  useEffect(() => {
    if (selected) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
    return () => (document.body.style.overflow = '')
  }, [selected])

  useEffect(() => {
    document.documentElement.lang = lang
  }, [lang])

  useEffect(() => {
    try {
      const saved = localStorage.getItem('userName')
      if (saved) setUserName(saved)
    } catch {}
  }, [])

  const toggleLang = () => setLang((prev) => (prev === 'ru' ? 'tt' : 'ru'))

  const startDialogue = (item) => {
    setActive(item)
    setSelected(null)
    setView('dialog')
  }
  const backHome = () => {
    setView('home')
    setActive(null)
  }
  const goHome = () => setView('home')
  const goAbout = () => setView('about')

  const onCardClick = (item) => {
    if (!userName) {
      setNeedName(true)
      return
    }
    setSelected(item)
  }

  const saveName = (name) => {
    const n = (name || '').trim()
    if (!n) return
    setUserName(n)
    try { localStorage.setItem('userName', n) } catch {}
    setNeedName(false)
  }

  return (
    <div className="app">
      {view !== 'dialog' && (
        <Header
          lang={lang}
          t={i18n[lang]}
          onToggleLang={toggleLang}
          userName={userName}
          onGoCharacters={goHome}
          onGoAbout={goAbout}
        />
      )}

      {view === 'home' && (
        <main className="container">
          <div className="grid">
            {items.map((item) => (
              <Card key={item.id} item={item} lang={lang} t={i18n[lang]} onClick={() => onCardClick(item)} />
            ))}
          </div>
        </main>
      )}

      {view === 'dialog' && active && (
        <main className="container">
          <Dialogue item={active} lang={lang} t={i18n[lang]} onBack={backHome} />
        </main>
      )}

      {view === 'about' && (
        <About t={i18n[lang]} />
      )}

      {selected && (
        <Modal
          item={selected}
          lang={lang}
          t={i18n[lang]}
          onClose={() => setSelected(null)}
          onPlay={startDialogue}
        />
      )}

      {needName && (
        <AuthName onCancel={() => setNeedName(false)} onSubmit={saveName} lang={lang} t={i18n[lang]} />
      )}
    </div>
  )
}
