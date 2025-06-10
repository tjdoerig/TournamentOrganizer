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

Das folgende C4 System Context Diagramm zeigt die Hauptkomponenten und Benutzer der Plattform:

```plantuml
@startuml C4_TournamentOrganizer
!includeurl https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title System Context Diagram - Tournament Organizer

Person(SuperAdmin, "Super Admin", "Systemweiter Zugriff - verwaltet alles")
Person(User, "Benutzer (authentifiziert)", "Organisator oder Teilnehmer mit Login")
Person(Guest, "Gast (Öffentlicher Benutzer)", "Kann Teams anmelden und öffentliche Turnierinfos sehen")

Container_Boundary(s1, "Tournament Organizer System") {
    Container(WebApp, "Tournament Organizer", "Web-App zur Verwaltung von Turnieren")

    Container(SQLDB, "SQL Server DB", "Speichert Benutzer, Turniere, Teams, Spiele")
    Container(AuthService, "Auth (.NET Identity)", "Verwaltet Benutzer und Rollen")
    Container(PDFService, "PDF Generator", "Erstellt PDF-Berichte und Spielpläne")
}

System_Ext(EmailService, "E-Mail-Dienst", "Sendet Turnierinformationen")
System_Ext(CalendarAPI, "Kalender-API (optional)", "Synchronisiert Spieltermine")

System_Ext(ZPLPrinter, "ZPL-Drucker", "Drucker, der ZPL-Befehle über Netzwerk empfängt")
System_Ext(TimeMeasurement, "Zeitmessanlage (RS232)", "Gerät zur Zeitmessung, kommuniziert via RS232")

Rel(SuperAdmin, WebApp, "Verwaltet alles")
Rel(User, WebApp, "Erstellt und verwaltet Turniere und Teams")
Rel(Guest, WebApp, "Meldet Teams an, sieht öffentliche Turniere")

Rel(WebApp, SQLDB, "Speichert & liest Daten")
Rel(WebApp, AuthService, "Authentifizierung & Rollen")
Rel(WebApp, PDFService, "Erstellt PDFs")
Rel(WebApp, EmailService, "Sendet E-Mails")
Rel(WebApp, CalendarAPI, "Synchronisiert Termine")

Rel(WebApp, ZPLPrinter, "Sendet ZPL-Druckaufträge", "ZPL")
Rel(WebApp, TimeMeasurement, "Kommuniziert via RS232", "RS232")

SHOW_LEGEND()
@enduml
