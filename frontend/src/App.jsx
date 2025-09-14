import React, { useState, useEffect } from 'react'
import { fetchItems, createStoryAndDialogue } from './api/client'
import Header from './components/Header/Header'
import Card from './components/Card/Card'
import Modal from './components/Modal/Modal'
import Dialogue from './components/Dialogue/Dialogue'
import AuthName from './components/AuthName/AuthName'
import About from './components/About/About'
import { i18n } from './i18n'
import { dialogues } from './data/dialogues'

export default function App() {
  const [selected, setSelected] = useState(null)
  const [lang, setLang] = useState('ru')
  const [view, setView] = useState('home') 
  const [active, setActive] = useState(null)
  const [userName, setUserName] = useState(null)
  const [needName, setNeedName] = useState(false)
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [storyLoading, setStoryLoading] = useState(false)

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
    let cancelled = false
    setLoading(true)
    setError(null)
    fetchItems()
      .then((list) => {
        if (!cancelled) { setItems(list); setLoading(false) }
      })
      .catch((e) => {
        if (!cancelled) { setError(e?.message || 'Load error'); setLoading(false) }
      })
    return () => { cancelled = true }
  }, [])

  useEffect(() => {
    try {
      const saved = localStorage.getItem('userName')
      if (saved) setUserName(saved)
    } catch {}
  }, [])

  const toggleLang = () => setLang((prev) => (prev === 'ru' ? 'tt' : 'ru'))

  const startDialogue = async (item) => {
    // Require a registered userId
    let userId
    try { userId = localStorage.getItem('userId') } catch {}
    if (!userId) {
      setNeedName(true)
      return
    }

    try {
      setStoryLoading(true)
      const personaName = item?.title?.ru || item?.title?.tt || ''
      const resp = await createStoryAndDialogue({ userId, personaName, context: '' })
      const d = resp?.dialogue || {}

      // Adapt backend MultiBranchDialogue -> app dialogues format
      const startId = 'start'
      const goodId = 'good0'
      const badId = 'bad0'
      const endId = 'end'
      const speaker = { ru: item?.title?.ru || '', tt: item?.title?.tt || '' }
      const nodes = {}

      // start node
      nodes[startId] = {
        speaker,
        text: { ru: d.initial_npc_phrase_ru || '', tt: d.initial_npc_phrase_tt || '' },
        options: (d.initial_options || []).slice(0, 4).map((o) => ({
          id: o.id,
          label: { ru: o.text_ru || '', tt: o.text_tt || '' },
          next: (o.type === 'good') ? goodId : badId,
        })),
      }

      // good branch node (first one if exists)
      const gb = Array.isArray(d.good_branches) && d.good_branches.length > 0 ? d.good_branches[0] : null
      nodes[goodId] = {
        speaker,
        text: { ru: gb?.npc_phrase_ru || '', tt: gb?.npc_phrase_tt || '' },
        options: (gb?.options || []).slice(0, 4).map((o) => ({
          id: o.id,
          label: { ru: o.text_ru || '', tt: o.text_tt || '' },
          next: endId,
        })),
      }

      // bad branch node (first one if exists)
      const bb = Array.isArray(d.bad_branches) && d.bad_branches.length > 0 ? d.bad_branches[0] : null
      nodes[badId] = {
        speaker,
        text: { ru: bb?.npc_phrase_ru || '', tt: bb?.npc_phrase_tt || '' },
        options: (bb?.options || []).slice(0, 4).map((o) => ({
          id: o.id,
          label: { ru: o.text_ru || '', tt: o.text_tt || '' },
          next: endId,
        })),
      }

      nodes[endId] = {
        speaker,
        text: { ru: '', tt: '' },
        options: [],
      }

      // Save into dialogues store under character id
      dialogues[item.id] = { start: startId, nodes }

      setActive(item)
      setSelected(null)
      setView('dialog')
    } catch (e) {
      console.error(e)
      alert('Не удалось начать историю: ' + (e?.message || 'ошибка'))
    } finally {
      setStoryLoading(false)
    }
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
          {loading && <p style={{ color: '#05624E' }}>Загрузка…</p>}
          {error && <p style={{ color: 'crimson' }}>Ошибка: {error}</p>}
          {!loading && !error && (
            <div className="grid">
              {items.map((item) => (
                <Card key={item.id} item={item} lang={lang} t={i18n[lang]} onClick={() => onCardClick(item)} />
              ))}
            </div>
          )}
        </main>
      )}

      {view === 'dialog' && active && (
        <main className="container">
          <Dialogue item={active} lang={lang} t={i18n[lang]} onBack={backHome} onToggleLang={toggleLang} />
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

      {storyLoading && (
        <div className="overlay" role="status" aria-live="polite" aria-busy="true">
          <div className="wait">
            <div className="wait__spinner" />
            <div className="wait__text">
              {lang === 'tt'
                ? 'Зинһар, көтегез — хикәя тудырыла…'
                : 'Пожалуйста, подождите — идёт генерация истории…'}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
