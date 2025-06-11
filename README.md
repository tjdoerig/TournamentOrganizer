# 🏆 Tournament Organizer

**Tournament Organizer** ist eine Webplattform zur einfachen Planung, Verwaltung und Durchführung von Turnieren für Mannschafts- oder Einzelsportarten. Die Anwendung basiert auf **.NET 9.0** und **Blazor** mit **MudBlazor** für ein modernes UI-Design.

---

## 🚀 Features

- Turniere erstellen und verwalten (KO, Round Robin, Gruppenphase)
- Teilnehmer- und Teamverwaltung (auch Gastzugang ohne Account)
- Spielplanerstellung mit Zeit- und Feldzuweisung
- Ergebniserfassung & automatische Ranglisten
- PDF-Reports: Spielplan, Schiedsrichterkarten, Teilnehmerlisten
- Rollenmodell mit Admins, Teilnehmern, Gästen
- Öffentliche Übersicht: Spielpläne und Tabellen

---

## 🧱 Tech Stack

| Komponente        | Technologie            |
|-------------------|------------------------|
| Frontend          | Blazor (MudBlazor)     |
| Backend           | ASP.NET Core 9.0       |
| Authentifizierung | ASP.NET Identity       |
| Datenbank         | SQL Server (EF Core)   |
| PDF-Export        | QuestPDF oder DinkToPdf|
| Hosting           | Azure / IIS / Docker   |

---

## 🛠️ Setup

### Voraussetzungen
- .NET SDK 9.0 (Preview oder später)
- Visual Studio 2022+ oder VS Code
- SQL Server (lokal oder Azure SQL)

### Projektstruktur (geplant)
- /src/Frontend  (Blazor WebApp)
- /src/Backend   (ASP.NET Core Web API)
- /src/Shared    (DTOs, Models, Services)
- /docs          (Dokumentation, Diagramme)

---

## 🏗️ Architektur
![C4_P1](https://github.com/user-attachments/assets/5a017239-7a94-44de-bbb9-9b7026c04a75)




