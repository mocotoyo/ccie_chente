# -*- coding: utf-8 -*-
"""
Script seguro UTF-8 Windows para generar README del roadmap CCIE Enterprise Infrastructure v1.1 ‚Äî Vicente
Genera 365 d√≠as con fases, actividades, recursos y formato Markdown
"""

import yaml

# Configuraci√≥n de fases (sin caracteres problem√°ticos)
fases = [
    {"nombre": "Fase 0", "emoji": ":memo:", "inicio": 1, "fin": 2, "descripcion": "Planeacion y preparacion"},
    {"nombre": "Fase 1", "emoji": ":arrows_counterclockwise:", "inicio": 3, "fin": 10, "descripcion": "Switching / L2-L3"},
    {"nombre": "Fase 2", "emoji": ":globe_with_meridians:", "inicio": 11, "fin": 18, "descripcion": "Routing avanzado / BGP / MPLS"},
    {"nombre": "Fase 3", "emoji": ":office:", "inicio": 19, "fin": 26, "descripcion": "Infraestructura empresarial / QoS / Multicast"},
    {"nombre": "Fase 4", "emoji": ":cloud:", "inicio": 27, "fin": 34, "descripcion": "SD-WAN / SD-Access"},
    {"nombre": "Fase 5", "emoji": ":robot:", "inicio": 35, "fin": 42, "descripcion": "Automatizacion / Python / Ansible"},
    {"nombre": "Fase 6", "emoji": ":wrench:", "inicio": 43, "fin": 50, "descripcion": "Integracion y labs largos"},
    {"nombre": "Fase 7", "emoji": ":checkered_flag:", "inicio": 51, "fin": 52, "descripcion": "Revision final / simulacros"},
]

# Actividades por fase
actividades = {
    "Fase 0": ["Descargar Blueprint CCIE EI v1.1", "Configurar tracker Notion", "Configurar laboratorio virtual",
               "Instalar imagenes IOS-XE / CSR", "Crear cuenta DevNet", "Definir calendario semanal", "Instalar Anki"],
    "Fase 1": ["Labs VLANs y STP", "Configurar EIGRP/OSPF mixto", "Debugging y show commands"],
    "Fase 2": ["Configurar BGP iBGP/eBGP", "Configurar MPLS y VRFs", "Labs de route policies"],
    "Fase 3": ["QoS end-to-end", "Multicast PIM-SM/DM", "Documentar troubleshooting"],
    "Fase 4": ["SD-WAN vManage + vEdge", "Policies de control y datos", "Simulacion de fallos"],
    "Fase 5": ["Python basico", "Ansible playbooks", "RESTCONF / NETCONF labs"],
    "Fase 6": ["Labs integrales 6-8h", "Diseno + Deploy + Operacion", "Fallas intencionales y resolucion"],
    "Fase 7": ["Repasar blueprint", "Simulacros finales", "Revision de comandos show/debug"]
}

# Recursos por actividad
recursos = {
    "Descargar Blueprint CCIE EI v1.1": "https://www.cisco.com/",
    "Configurar tracker Notion": "https://www.notion.so/",
    "Configurar laboratorio virtual": "https://www.eve-ng.net/",
    "Instalar imagenes IOS-XE / CSR": "https://www.cisco.com/",
    "Crear cuenta DevNet": "https://developer.cisco.com/",
    "Definir calendario semanal": "",
    "Instalar Anki": "https://apps.ankiweb.net/",
}

# Generar README
with open("README_generated.md", "w", encoding="utf-8") as f:
    f.write("# Ìºê Roadmap CCIE Enterprise Infrastructure v1.1 ‚Äî Vicente\n\n")
    f.write("Bienvenido al **roadmap de 365 d√≠as**, organizado por fases, labs y checklists.\n\n")
    f.write("## Ì≥Ç Contenido del repo\n\n")
    f.write("- `generate_readme.py` ‚Üí Genera README completo de 365 d√≠as.\n")
    f.write("- `vicente-roadmap-365.yml` ‚Üí YAML listo para importar en GitHub Projects.\n")
    f.write("- Recursos y documentacion de apoyo.\n\n")
    
    f.write("## Ì∫Ä Acceso al Project en GitHub\n\n")
    f.write("[‚û°Ô∏è Ver Roadmap en GitHub Projects](https://github.com/users/mocotoyo/projects/1)\n\n")
    
    f.write("## Ì¥π Fases y colores\n\n")
    f.write("| Fase | Emoji | Semanas | Color sugerido |\n")
    f.write("|------|-------|---------|----------------|\n")
    for fase in fases:
        color = "Ì¥µ" if "0" in fase["nombre"] else "Ìø¢"
        f.write(f"| {fase['emoji']} {fase['nombre']} | {fase['emoji']} | {fase['inicio']}-{fase['fin']} | {color} |\n")
    
    f.write("\n## Ì≥Ö Vista diaria (resumen de ejemplo)\n\n")
    f.write("| D√≠a | Fase | Actividad | Emoji | Recurso | Estado |\n")
    f.write("|-----|------|-----------|-------|--------|--------|\n")
    
    day = 1
    while day <= 365:
        for fase in fases:
            for act in actividades.get(fase["nombre"], []):
                if day > 365:
                    break
                recurso = recursos.get(act, "")
                f.write(f"| {day} | {fase['emoji']} {fase['nombre']} | {act} | {fase['emoji']} | {recurso} | ‚è≥ |\n")
                day += 1
            if day > 365:
                break
    
    f.write("\n## Ì≤° Tips de uso\n\n")
    f.write("- Marca cada tarjeta: ‚è≥ Pendiente / Ì¥Ñ En progreso / ‚úÖ Completado\n")
    f.write("- Usa emojis de fase y lab para identificar rapidamente el contenido\n")
    f.write("- Consulta Calendar / Timeline para planificar bloques de estudio\n")
    f.write("- Documenta errores y soluciones de tus labs directamente en las tarjetas\n\n")
    
    f.write("## Ì≥ö Bibliografia general\n\n")
    f.write("- *Routing TCP/IP Vol 1 & 2* ‚Äî Jeff Doyle\n")
    f.write("- *MPLS Fundamentals* ‚Äî Luc De Ghein\n")
    f.write("- *CCIE Enterprise Infrastructure v1.1 Official Cert Guide* ‚Äî Cisco\n\n")
    
    f.write("## Ì≤™ Motivacion diaria\n\n")
    f.write("> ‚ÄúVicente, tu disciplina define tu exito. Cada lab, cada tarjeta, cada dia cuenta. Mantente constante, documenta todo y conquistaras tu CCIE EI v1.1.‚Äù\n")

print("‚úÖ README_generated.md creado correctamente con 365 d√≠as.")

