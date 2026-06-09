# NemoClaw Live Demo Script
> **Date:** June 2026 · **Version:** docker-compose · **LLM:** Nemotron 3 Super 120b A12b

---

## Pre-Demo Setup

Configure the 3 Telegram accounts in `docker-compose/scripts/identity/SOUL.md` under the Authorization table:

| Telegram ID | Account | Name | Role | store_id | Store |
|-------------|---------|------|------|----------|-------|
| _(your ID 1)_ | Account 1 | Connie | data_analyst | — | — |
| _(your ID 2)_ | Account 2 | Paula | store_manager | 2 | NemoClaw Barcelona |
| _(your ID 3)_ | Account 3 | Sergio | country_manager | — | Spain |

> **Suggested demo order:** Data Analyst → Store Manager → Country Manager.  
> This builds tension: start with read-only, escalate to scoped writes, end with full power.

---

---

# 👩‍💻 DATA ANALYST

**Narrative:** *"Data analyst has full visibility across all 5 stores in Spain — but read-only access. She's the insight engine."*

**RBAC:** `data_analyst` · Read-only across all stores · Zero write access (blocked before any DB call)

---

### 📊 Analytics & Inventory

| # | Type in Telegram | What it showcases |
|---|---|---|
| 1 | `Show me which items are below reorder level across all stores` | Cross-chain LowStockAlerts view, all 5 stores |
| 2 | `Show me inventory of Running Shoe ClimaTex in all stores` | Multi-store inventory view (takes a moment — good to warn audience) |
| 3 | `What are the most urgent low-stock items, grouped by store?` | Cross-store operational overview |

---

### 💰 Sales & Revenue

| # | Type in Telegram | What it showcases |
|---|---|---|
| 4 | `Compare monthly sales across all stores` | SalesPerformanceByStore view, cross-chain trends |
| 5 | `Which store had the highest revenue last month?` | Chain-wide ranking (slightly slower — worth the wait) |
| 6 | `What are our best-selling products across all stores?` | TopProductsByRevenue view |
| 7 | `Top 10 products by revenue in the Footwear category` | Category drill-down |
| 8 | `Show me sales from last week across all stores` | Recent performance pulse |
| 9 | `What's the average order value per store?` | Store benchmarking KPI |

---

### 👥 CRM & Customers

| # | Type in Telegram | What it showcases |
|---|---|---|
| 10 | `Who are our top 5 customers by lifetime value?` | Customer360 view |
| 11 | `Show me customers who haven't purchased in the last 3 months` | Churn / re-engagement candidates |
| 12 | `Show me purchases and total spent per customer this month` | CRM deep dive ⚠️ may fail |
| 13 | `Give me the profile of customer Silvia Gil Reyes` | Customer360 profile (preferred store: Barcelona) |
| 14 | `Show his most recent order` | Order + OrderItems join |
| 15 | `Which gender segment generates the most revenue chain-wide?` | Demographic insight |

---

### 🌱 Sustainability (Bonus - if time allows)

| # | Type in Telegram | What it showcases |
|---|---|---|
| 16 | `Which products have the highest sustainability score?` | ESG angle — sustainability_score |

---

### 🚫 Permission Denied - the "gotcha" moment

> **Presenter tip:** *"Now let's say María wants to take action on what she sees…"*

| # | Type in Telegram | Expected response |
|---|---|---|
| 19 | `Reorder 20 units of Running Shoe ClimaTex size M color White for Barcelona` | ❌ **"You have read-only access."** — denied before any DB call |
| 20 | `Transfer 10 units of Running Shoe ClimaTex size M color White from Madrid to Barcelona` | ❌ **"You have read-only access."** — same instant denial |

> *"The system doesn't even try to execute the query. The denial is pre-emptive - role checked first."*

---

---

# 🏪 STORE MANAGER

**Narrative:** *"Now let's switch to -, store manager in -. She can see everything across the chain, but she can only act within her own store."*

**RBAC:** `store_manager` · Read all stores · Write only Barcelona (store_id=2) · Transfer FROM Barcelona only · Can approve reorder requests for Barcelona

---

### 📦 Barcelona Inventory & Promotions

| # | Type in Telegram | What it showcases |
|---|---|---|
| 1 | `Which products are under reorder level?` | LowStockAlerts auto-filtered to Barcelona → store by default |
| 2 | `Show me all active promotions right now` | ActivePromotions view — both chain-wide and Barcelona-specific |
| 3 | `Which promotions have driven the most discount spend this season?` | Promotion ROI — joins OrderItems on promotion_id |

---

### 📈 Barcelona Performance & Comparisons

| # | Type in Telegram | What it showcases |
|---|---|---|
| 4 | `How is my store performing this month?` | SalesPerformanceByStore for Barcelona |
| 5 | `Show me monthly revenue for the past 7 months` | Medium-term trend for Barcelona |
| 6 | `What are the most recent orders placed today? This week?` | Operational awareness |
| 7 | `Which products generated the most revenue in my store?` | Barcelona TopProducts ⚠️ may take one fail |
| 8 | `How do Barcelona's best-sellers compare to the chain-wide performance?` | Cross-store comparison read (allowed) |
| 9 | `Compare my store's performance this month vs Madrid` | Direct head-to-head |
| 10 | `Which customers bought the most in my store this month?` | Barcelona CRM pulse |
| 11 | `Show inventory of Straight Jean UrbanStep` | Barcelona product inventory → store by default ⚠️ may take one fail |

---

### ✅ Actions - Barcelona (ALLOWED)

> **Presenter tip:** *"Now Paula sees a low-stock alert and takes action."*

**A1 - Show pending reorder requests**

```
Show me pending reorder requests for my store
```
> ⚠️ The first response sometimes shows oddly formatted output — just ask again: `Show pending reorder requests for Barcelona`.  Second try is clean ✅

---

**A2 - Approve a pending reorder request for Barcelona**

```
Approve reorder request number 13 for my store
```
> ✅ Store managers CAN approve their own store's reorder requests.

---

**A3 - Reorder for Barcelona (own store - ALLOWED)**

> Specify product, size, color, and quantity to avoid the agent asking back.

```
Reorder 30 units of Running Shoe EcoWear size M color Camel for my store
```
> ✅ Success. Confirm the reorder request was created.

---

**A4 - Transfer FROM Barcelona (own store - ALLOWED)**

> Specify all details upfront.

```
Transfer 8 units of Running Shoe ClimaTex size M color White from Barcelona to the Sevilla store
```
> ✅ Transfer request created successfully (pending approval by country manager).

---

### 🚫 Permission Denied - scoped writes

> **Presenter tip:** *"What if Paula tries to help out another store?"*

**A5 - Try to reorder for Valencia (another store — FORBIDDEN)**

```
Reorder 30 units of Running Shoe Ecowear size M color camel for the Valencia store
```
> ❌ **"You can only reorder for your own store (Barcelona)."** - denied before exec

---

**A6 - Try to transfer FROM Madrid (not her store — FORBIDDEN)**

```
Transfer 8 units of Running Shoe Climatex size M color Black from the Madrid store to the Valencia store
```
> ❌ **"You can only transfer from your own store (Barcelona)."** - denied before exec

> *"Paula can request stock from Madrid - but she can't initiate a transfer on Madrid's behalf. That's the country manager's job."*

---

**A7 - Try to approve the transfer (FORBIDDEN)**

```
Can you approve the transfer I just did?
```
> ❌ **"Only a country manager can approve inventory transfers."** - denied before exec

---

---

# 👔 COUNTRY MANAGER

**Narrative:** *"Finally, let's look at Sergio, country manager for Spain. Full read and write access across all 5 stores. And the only role that can approve inter-store transfers."*

**RBAC:** `country_manager` · Read + Write across all stores · Only role that can approve InventoryTransfers

---

### 🌍 Strategic Overview

| # | Type in Telegram | What it showcases |
|---|---|---|
| 1 | `Compare monthly sales across all stores` | Executive dashboard view |
| 2 | `Which store had the highest revenue last month?` | Performance ranking (slightly slower — worth it) |
| 3 | `What are the most urgent low-stock items across all stores?` | Chain-wide operational risk |
| 4 | `Which items need reorder across the entire chain?` | Full LowStockAlerts, all stores |
| 5 | `What are our best-selling products across Spain?` | TopProductsByRevenue, all stores |
| 6 | `Top 10 products by revenue in the Footwear category` | Category leadership |
| 7 | `Show me all active promotions and which stores they apply to` | Promotion portfolio overview |
| 8 | `Show me inventory of Running Shoe ClimaTex across all stores` | Cross-chain stock distribution |
| 9 | `Which brand generates the most revenue across all stores?` | _(New)_ Brand portfolio insight |
| 10 | `Which store has the most pending reorder requests right now?` | _(New)_ Urgency triage — who needs attention? |
| 11 | `Who are our top 5 customers by lifetime value across Spain?` | VIP customer list |

---

### ✅ Actions - Full Chain (ALL ALLOWED)

**A1 - Show all pending transfers**

```
Show me all pending transfers waiting for approval
```
> ✅ Lists all pending InventoryTransfers across all stores (including the Madrid→Barcelona one Paula requested).

---

**A2 - Approve a pending inter-store transfer (COUNTRY MANAGER EXCLUSIVE)**

> **Presenter tip:** *"Remember the transfer Paula initiated from Barcelona to Valencia, or the one Madrid requested to Barcelona? Sergio is the only one who can approve these."*

```
Approve transfer number 1
```
> ✅ Transfer approved — stock moves from Madrid to Barcelona. **This is the only role that can do this.**  
> Compare: if Paula had tried this earlier, it would have been denied.

---

**A3 - Reorder for any store**

> Sergio can reorder for any store — no restriction.

```
Reorder 25 units of Puffer Jacket Neofit size L color Black for the Sevilla store
```
> ✅ Works for any store — no restriction on Sergio.

---

**A4 - Approve the reorder request**

```
Approve the reorder request I just did
```
> ✅ Reorder approved. Country managers can approve reorder requests for any store.

---

---

## 🎯 Permission Matrix Summary (for slide/handout)

| Capability | Data Analyst | Store Manager (Barcelona) | Country Manager |
|---|:---:|:---:|:---:|
| Read own store data | ✅ | ✅ | ✅ |
| Read all stores data | ✅ | ✅ | ✅ |
| Reorder for own store | ❌ | ✅ | ✅ |
| Reorder for other stores | ❌ | ❌ | ✅ |
| Transfer FROM own store | ❌ | ✅ | ✅ |
| Transfer FROM other stores | ❌ | ❌ | ✅ |
| Approve reorder requests (own store) | ❌ | ✅ | ✅ |
| Approve inter-store transfers | ❌ | ❌ | ✅ |

---

## ⚡ Presenter Tips

- **"Across all stores"** - adding this phrase forces the agent to remove the default per-store filter. Great to show the scoping behavior.
- **Default scoping** - when Paula asks "which products need reorder?" without qualifying, the agent auto-filters to Barcelona (store_id=2). You can demonstrate this, then ask "and across all stores?" to contrast.
- **Slow queries** - store revenue comparisons (#7 in most sections) take a few seconds. Warn the audience: *"This one joins a few tables - give it a moment."*
- **Reorder actions** - always specify product name, size, color, and quantity upfront to avoid the agent asking back (which breaks demo flow).
- **Pending reorder display** - if the first response looks oddly formatted, just repeat the question. Second try is consistently clean.
- **Transfer approval narrative** - the strongest demo moment is: Paula initiates a transfer (Act 2), Sergio approves it (Act 3). Pre-stage this by doing Paula's transfer first.
