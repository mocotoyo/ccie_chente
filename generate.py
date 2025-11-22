import yaml
from datetime import datetime, timedelta

# Configuración inicial
start_date = datetime(2025, 10, 17)
phases = [
    ("Fase 0: Planeación y Preparación", 14),
    ("Fase 1: Fundamentos Switching / L2-L3", 56),
    ("Fase 2: Routing Avanzado / BGP", 56),
    ("Fase 3: Infraestructura Empresarial / QoS", 56),
    ("Fase 4: SD-WAN y SD-Access", 56),
    ("Fase 5: Automatización y Programmability", 56),
    ("Fase 6: Integración / Labs reales", 56),
    ("Fase 7: Revisión final / Mindset CCIE", 14),
]

# Plantilla de nota por fase (puedes personalizar cada fase si quieres)
notes = {
    "Fase 0: Planeación y Preparación": "Planeación y preparación del laboratorio y herramientas",
    "Fase 1: Fundamentos Switching / L2-L3": "Labs y estudio de Switching y Layer 2/3",
    "Fase 2: Routing Avanzado / BGP": "Routing avanzado, BGP, MPLS, VRF",
    "Fase 3: Infraestructura Empresarial / QoS": "Campus, QoS, multicast, gestión",
    "Fase 4: SD-WAN y SD-Access": "SD-WAN, SD-Access, políticas de control",
    "Fase 5: Automatización y Programmability": "Python, Ansible, RESTCONF, telemetría",
    "Fase 6: Integración / Labs reales": "Integración completa de protocolos y troubleshooting",
    "Fase 7: Revisión final / Mindset CCIE": "Repaso, simulacros y mindset CCIE",
}

# Construcción del YAML
project = {
    "name": "Roadmap CCIE Enterprise Infrastructure v1.1 — Vicente",
    "body": "Roadmap completo de 365 días para CCIE EI v1.1 con fases, labs y checklists.",
    "start-date": "2025-10-17",
    "due-date": "2026-10-16",
    "fields": [
        {"name": "Phase", "type": "single_select", "options": [p[0] for p in phases]},
        {"name": "Status", "type": "single_select", "options": ["Pendiente", "En progreso", "Completo"]}
    ],
    "cards": []
}

current_date = start_date
for phase, days in phases:
    for _ in range(days):
        card = {
            "note": notes[phase],
            "phase": phase,
            "status": "Pendiente",
            "due-date": current_date.strftime("%Y-%m-%d")
        }
        project["cards"].append(card)
        current_date += timedelta(days=1)

# Guardar YAML
with open("vicente-roadmap-365.yml", "w") as f:
    yaml.dump(project, f, sort_keys=False, allow_unicode=True)

print("Archivo vicente-roadmap-365.yml generado con éxito ✅")

