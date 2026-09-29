# Lesson 04 — Sequential Pattern dan Spurious Discovery

## Problem dan why

Urutan A→B→C membawa informasi yang hilang bila data diubah menjadi set. Namun makin banyak sequence/pattern diuji, makin besar peluang “menarik” secara kebetulan.

## Mechanism

Sequential mining memerlukan entity, ordered event time, event type, dan definisi window/gap. Pattern support menghitung entity/sequence yang memuat pola, bukan row mentah. Validasi harus menjaga order dan memisahkan discovery dari confirmation.

## Alternatives dan assumptions

Transition matrix cocok untuk langkah satu; rule engine untuk urutan domain-known; sequence model untuk prediction kompleks. Pattern mining mengasumsikan logging/order cukup benar dan observation comparable.

## Failure/debug/evidence

Timestamp tie, duplicate/retry, late event, serta device reboot dapat menciptakan sequence palsu. Audit event contract, deduplicate, sort per entity, dan uji pada periode/site berbeda. Koreksi multiple testing atau nyatakan eksploratif.

## Workplace dan checkpoint

Dipakai pada clickstream, maintenance event, dan alarm cascade. Definisikan grain sequence, gap, support denominator, holdout, serta batas causal claim.
