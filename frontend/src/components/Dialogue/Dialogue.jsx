import React, { useMemo, useState } from 'react'
import { dialogues } from '../../data/dialogues'
import Button from '../Button/Button'

export default function Dialogue({ item, lang = 'ru', t, onBack }) {
  const dlg = dialogues[item?.id] || null
  const [nodeId, setNodeId] = useState(dlg?.start || null)
  const node = useMemo(() => (dlg ? dlg.nodes[nodeId] : null), [dlg, nodeId])

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

  const options = node?.options || []

  return (
    <div className="dialog">
      <div className="dialog__frame">
        <img className="dialog__image" src={item.image} alt={item.title?.[lang] || ''} />
        <div className="dialog__box">
          <div className="dialog__line">
            <span className="dialog__speaker">{node?.speaker?.[lang] || item.title?.[lang] || ''}:</span>
            <span className="dialog__text"> {node?.text?.[lang] || ''}</span>
          </div>
          <div className="dialog__choices">
            {options.slice(0,4).map((opt) => (
              <Button key={opt.id} fullWidth onClick={() => setNodeId(opt.next)}>
                {opt.label?.[lang] || ''}
              </Button>
            ))}
            {options.length === 0 && (
              <div className="dialog__back">
                <Button onClick={onBack}>{t?.back || 'Назад'}</Button>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

