# Kolada – Dagligvaruhandel (försäljning)

Denna MCP-server (Model Context Protocol) ger strukturerad åtkomst till
Koladas öppna API för KPI **N52001 – Försäljning i dagligvaruhandel**.

KPI:n avser:
**Försäljning i dagligvaruhandel inklusive moms, miljoner kronor**  
och används främst för analys på kommunnivå i Sverige.

## Datakälla
- Kolada öppna API: https://api.kolada.se/v3
- KPI: **N52001 – Försäljning i dagligvaruhandel**

All data hämtas oförändrad direkt från Kolada.

## Vad denna MCP gör
- Tillhandahåller ett MCP-verktyg för att hämta metadata om KPI:er
- Fungerar som ett tunt lager ovanpå Koladas officiella API
- Säkerställer spårbarhet till originalkälla och definitioner

## MCP-endpoint

```
/mcp
```
