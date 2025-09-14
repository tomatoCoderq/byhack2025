import React, { useEffect, useMemo, useRef, useState } from 'react'
import { dialogues } from '../../data/dialogues'
import Button from '../Button/Button'
import { generateEnding } from '../../api/client'

export default function Dialogue({ item, lang = 'ru', t, onBack, onToggleLang }) {
  const dlg = dialogues[item?.id] || null
  const [nodeId, setNodeId] = useState(dlg?.start || null)
  const node = useMemo(() => (dlg ? dlg.nodes[nodeId] : null), [dlg, nodeId])

  // Track start phrases and visited NPC phrases
  const [startRu, setStartRu] = useState('')
  const [startTt, setStartTt] = useState('')
  const [visitedRu, setVisitedRu] = useState([])
  const [visitedTt, setVisitedTt] = useState([])
  const [ending, setEnding] = useState(null)
  const [endingLoading, setEndingLoading] = useState(false)
  const [endingError, setEndingError] = useState('')
  const endingRequested = useRef(false)

  if (!dlg) {
    return (
      <div className="dialog">
        <div className="dialog__box">{t?.noDialogue || 'Диалог недоступен.'}</div>
        <div className="dialog__controls">
          <Button side="right" onClick={onBack}>{t?.back || 'Назад'}</Button>
        </div>
      </div>
    )
  }

  // Initialize on dialogue load
  useEffect(() => {
    if (!dlg) return
    const s = dlg.start
    const startNode = dlg.nodes?.[s]
    setStartRu(startNode?.text?.ru || '')
    setStartTt(startNode?.text?.tt || '')
    setVisitedRu([])
    setVisitedTt([])
    setEnding(null)
    setEndingError('')
    endingRequested.current = false
  }, [dlg])

  // Collect visited NPC phrases (exclude start and end)
  useEffect(() => {
    if (!dlg || !nodeId) return
    if (nodeId === dlg.start) return
    if (nodeId === 'end') return
    const n = dlg.nodes?.[nodeId]
    if (!n) return
    const ru = n.text?.ru || ''
    const tt = n.text?.tt || ''
    if (ru) setVisitedRu((arr) => [...arr, ru])
    if (tt) setVisitedTt((arr) => [...arr, tt])
  }, [dlg, nodeId])

  // Request ending when at end node
  useEffect(() => {
    if (!dlg || nodeId !== 'end' || endingRequested.current) return
    endingRequested.current = true
    setEndingLoading(true)
    setEndingError('')
    const persona = item?.title?.ru || item?.title?.tt || ''
    generateEnding({
      style: null,
      persona,
      start_ru: startRu,
      start_tt: startTt,
      visited_summary_ru: visitedRu.length ? visitedRu : [''],
      visited_summary_tt: visitedTt.length ? visitedTt : [''],
    })
      .then((res) => setEnding(res))
      .catch((e) => setEndingError(e?.message || 'Failed to generate ending'))
      .finally(() => setEndingLoading(false))
  }, [dlg, nodeId, item?.title?.ru, item?.title?.tt, startRu, startTt, visitedRu, visitedTt])

  const options = node?.options || []

  return (
    <>
    {!endingLoading && (
    <div className="dialog">
      <div className="dialog__frame">
        <img className="dialog__image" src={item.image} alt={item.title?.[lang] || ''} />
        <div className="dialog__box">
          {nodeId !== 'end' && (
            <div className="dialog__line">
              <div className="dialog__header">
                <span className="dialog__speaker">{node?.speaker?.[lang] || item.title?.[lang] || ''}:</span>
                <button
                  className="lang-toggle"
                  type="button"
                  onClick={onToggleLang}
                  aria-label={lang === 'ru' ? 'Сменить язык на татарский' : 'Рус теленә күчү'}
                  title={lang === 'ru' ? 'Сменить язык на татарский' : 'Рус теленә күчү'}
                >
                  <img className="lang-flag" src={lang === 'ru' ? '/russia.png' : '/tatarstan.png'} alt="" aria-hidden="true" />
                </button>
              </div>
              <span className="dialog__text"> {node?.text?.[lang] || ''}</span>
            </div>
          )}
          <div className="dialog__choices">
            {options.slice(0,4).map((opt) => (
              <Button key={opt.id} fullWidth onClick={() => setNodeId(opt.next)}>
                {opt.label?.[lang] || ''}
              </Button>
            ))}
            {options.length === 0 && (
              <>
                {endingLoading && (
                  <div style={{ color: '#05624E', margin: '8px 0' }}>
                    {lang === 'tt' ? 'Тәмамлау тудырыла…' : 'Генерация концовки…'}
                  </div>
                )}
                {endingError && (
                  <div style={{ color: '#b00020', margin: '8px 0' }}>{endingError}</div>
                )}
                {ending && (
                  <div className="dialog__full" style={{ display: 'grid', gap: 8, margin: '8px 0' }}>
                    <div className="dialog__line">
                      <div className="dialog__header">
                        <span className="dialog__speaker">{item.title?.[lang] || ''}:</span>
                        <button
                          className="lang-toggle"
                          type="button"
                          onClick={onToggleLang}
                          aria-label={lang === 'ru' ? 'Сменить язык на татарский' : 'Рус теленә күчү'}
                          title={lang === 'ru' ? 'Сменить язык на татарский' : 'Рус теленә күчү'}
                        >
                          <img className="lang-flag" src={lang === 'ru' ? '/russia.png' : '/tatarstan.png'} alt="" aria-hidden="true" />
                        </button>
                      </div>
                      <span className="dialog__text"> {ending?.[`npc_phrase_${lang}`] || ''}</span>
                    </div>
                    <div className="dialog__ending-text" style={{ whiteSpace: 'pre-wrap' }}>
                      {ending?.[`final_text_${lang}`] || ''}
                    </div>
                  </div>
                )}
                <div className="dialog__back">
                  <Button onClick={onBack}>{t?.back || 'Назад'}</Button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
    )}
    {endingLoading && (
      <div className="overlay" role="status" aria-live="polite" aria-busy="true">
        <div className="wait">
          <div className="wait__spinner" />
          <div className="wait__text">
            {lang === 'tt'
              ? 'Зинһар, көтегез — финал тудырыла…'
              : 'Пожалуйста, подождите — генерируется финал истории…'}
          </div>
        </div>
      </div>
      )}
    </>
  )
}
