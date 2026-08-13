html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3ra Estrategia: Priorización de Tareas</title>
    <style>
        :root {
            --covey-q1: #156049;
            --covey-q2: #279371;
            --covey-q3: #3F9089;
            --covey-q4: #104938;
            --axis-color: #104938;
            --modal-bg: #D1DE8C;
            --modal-text: #104938;
            --abc-bg: #F4F9F4;
            --abc-border: #279371;
            --font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-family);
            background-color: #f8faf9;
            color: #2c3e50;
            width: 100vw;
            height: 100vh;
            overflow-x: hidden;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .container {
            max-width: 1200px;
            width: 100%;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            padding: 24px;
        }

        header {
            text-align: center;
            margin-bottom: 20px;
            border-bottom: 2px solid #eef2f0;
            padding-bottom: 15px;
        }

        h1 {
            color: var(--axis-color);
            font-size: 1.8rem;
            margin-bottom: 8px;
        }

        .intro-text {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #4a5568;
            max-width: 1000px;
            margin: 0 auto;
        }

        /* Layout Grid for Widescreen / Landscape */
        .main-content {
            display: grid;
            grid-template-columns: 1fr;
            gap: 24px;
            margin-bottom: 20px;
        }

        /* Matrix Section */
        .matrix-section {
            position: relative;
            padding: 20px 10px 10px 40px;
        }

        .matrix-title {
            text-align: center;
            color: var(--axis-color);
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Axis Labels */
        .y-axis-label {
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%) rotate(-90deg);
            transform-origin: center;
            color: var(--axis-color);
            font-weight: bold;
            font-size: 1rem;
            letter-spacing: 1px;
            white-space: nowrap;
        }

        .x-axis-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            color: var(--axis-color);
            font-weight: bold;
            font-size: 0.95rem;
            padding: 0 5px;
        }

        /* Matrix Grid 2x2 */
        .matrix-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 12px;
            aspect-ratio: 16 / 9;
            max-height: 420px;
            width: 100%;
        }

        .quadrant {
            border-radius: 10px;
            padding: 20px;
            color: #ffffff;
            cursor: pointer;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            opacity: 0;
            animation: fadeIn 0.6s ease forwards;
        }

        .quadrant:hover {
            transform: translateY(-4px) scale(1.01);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }

        /* Quadrant Colors & Sequence Animation */
        .quadrant-1 {
            background-color: var(--covey-q1);
            animation-delay: 0.2s;
        }

        .quadrant-2 {
            background-color: var(--covey-q2);
            animation-delay: 0.5s;
        }

        .quadrant-3 {
            background-color: var(--covey-q3);
            animation-delay: 0.8s;
        }

        .quadrant-4 {
            background-color: var(--covey-q4);
            animation-delay: 1.1s;
        }

        .quadrant-num {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            opacity: 0.9;
            margin-bottom: 4px;
            font-weight: 600;
        }

        .quadrant-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 6px;
        }

        .quadrant-subtitle {
            font-size: 0.9rem;
            opacity: 0.95;
            font-style: italic;
        }

        .click-hint {
            margin-top: 10px;
            font-size: 0.75rem;
            background: rgba(255, 255, 255, 0.2);
            padding: 4px 10px;
            border-radius: 12px;
            font-weight: 500;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(15px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* ABC Section */
        .abc-section {
            background-color: var(--abc-bg);
            border: 2px solid var(--abc-border);
            border-radius: 10px;
            padding: 20px;
            margin-top: 10px;
        }

        .abc-header {
            text-align: center;
            color: var(--axis-color);
            margin-bottom: 15px;
        }

        .abc-header h2 {
            font-size: 1.3rem;
        }

        .abc-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
        }

        .abc-card {
            background: #ffffff;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border-top: 4px solid var(--abc-border);
        }

        .abc-badge {
            display: inline-block;
            width: 30px;
            height: 30px;
            line-height: 30px;
            text-align: center;
            background: var(--covey-q2);
            color: white;
            font-weight: bold;
            border-radius: 50%;
            margin-bottom: 8px;
        }

        .abc-card h3 {
            color: var(--axis-color);
            font-size: 1rem;
            margin-bottom: 6px;
        }

        .abc-card p {
            font-size: 0.85rem;
            line-height: 1.4;
            color: #4a5568;
        }

        /* Extra Strategy: Tracy */
        .tracy-card {
            background: #edf6f2;
            border-left: 5px solid var(--covey-q1);
            padding: 15px 20px;
            border-radius: 6px;
            margin-top: 15px;
            font-size: 0.9rem;
            line-height: 1.4;
            color: var(--axis-color);
        }

        .tracy-card strong {
            color: var(--covey-q1);
        }

        /* Modal / Ventana Emergente */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
            z-index: 1000;
        }

        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }

        .modal-content {
            background-color: var(--modal-bg);
            color: var(--modal-text);
            width: 90%;
            max-width: 550px;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            position: relative;
            transform: scale(0.9);
            transition: transform 0.3s ease;
            border: 2px solid var(--axis-color);
        }

        .modal-overlay.active .modal-content {
            transform: scale(1);
        }

        .close-btn {
            position: absolute;
            top: 12px;
            right: 15px;
            background: none;
            border: none;
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--modal-text);
            cursor: pointer;
            line-height: 1;
        }

        .modal-header {
            border-bottom: 2px solid rgba(16, 73, 56, 0.2);
            padding-bottom: 10px;
            margin-bottom: 15px;
        }

        .modal-title {
            font-size: 1.4rem;
            font-weight: bold;
        }

        .modal-subtitle {
            font-size: 0.9rem;
            font-weight: 600;
            opacity: 0.9;
        }

        .modal-body {
            font-size: 0.95rem;
            line-height: 1.5;
        }

        .modal-section-title {
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 4px;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
        }

        .modal-body ul {
            padding-left: 20px;
            margin-bottom: 10px;
        }

        .action-box {
            background: rgba(255, 255, 255, 0.6);
            padding: 10px 14px;
            border-radius: 6px;
            font-weight: bold;
            margin-top: 12px;
            border-left: 4px solid var(--axis-color);
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .abc-grid {
                grid-template-columns: 1fr;
            }
            .matrix-grid {
                aspect-ratio: auto;
                height: 380px;
            }
            .quadrant-title {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>Tercera Estrategia: Priorización de Tareas</h1>
            <p class="intro-text">
                Si la planificación responde a la pregunta <em>¿qué debo hacer?</em>, la priorización responde a <strong>¿qué debo hacer primero?</strong> La priorización es el núcleo de la administración del tiempo porque reconoce una realidad inevitable: el tiempo disponible es siempre menor que la suma de todas las tareas pendientes, por lo que elegir en qué invertirlo es una decisión de alto impacto (Claessens et al., 2007).
            </p>
        </header>

        <div class="main-content">
            <!-- Covey Matrix Interactive Section -->
            <div class="matrix-section">
                <div class="matrix-title">Matriz Urgente - Importante de Covey (2015)</div>
                
                <div class="y-axis-label">▲ IMPORTANCIA (Arriba: Importante / Abajo: No importante)</div>
                
                <div class="x-axis-container">
                    <span>◄ URGENTE</span>
                    <span>NO URGENTE ►</span>
                </div>

                <div class="matrix-grid">
                    <!-- Quadrant I -->
                    <div class="quadrant quadrant-1" onclick="openModal(1)">
                        <span class="quadrant-num">Cuadrante I</span>
                        <div class="quadrant-title">Crisis</div>
                        <div class="quadrant-subtitle">Urgente e Importante</div>
                        <span class="click-hint">Haz clic para detalles</span>
                    </div>

                    <!-- Quadrant II -->
                    <div class="quadrant quadrant-2" onclick="openModal(2)">
                        <span class="quadrant-num">Cuadrante II</span>
                        <div class="quadrant-title">Planificación</div>
                        <div class="quadrant-subtitle">Importante, No Urgente</div>
                        <span class="click-hint">Haz clic para detalles</span>
                    </div>

                    <!-- Quadrant III -->
                    <div class="quadrant quadrant-3" onclick="openModal(3)">
                        <span class="quadrant-num">Cuadrante III</span>
                        <div class="quadrant-title">Interrupciones</div>
                        <div class="quadrant-subtitle">Urgente, No Importante</div>
                        <span class="click-hint">Haz clic para detalles</span>
                    </div>

                    <!-- Quadrant IV -->
                    <div class="quadrant quadrant-4" onclick="openModal(4)">
                        <span class="quadrant-num">Cuadrante IV</span>
                        <div class="quadrant-title">Evasión</div>
                        <div class="quadrant-subtitle">No Urgente, No Importante</div>
                        <span class="click-hint">Haz clic para detalles</span>
                    </div>
                </div>
            </div>

            <!-- Lakein ABC Method Section -->
            <div class="abc-section">
                <div class="abc-header">
                    <h2>El Método ABC de Lakein (1973)</h2>
                    <p style="font-size: 0.9rem; color: #4a5568; margin-top: 4px;">Sistema de priorización sistemática según el valor de cada actividad</p>
                </div>
                <div class="abc-grid">
                    <div class="abc-card">
                        <span class="abc-badge">A</span>
                        <h3>Tareas "A" - Máximo Valor</h3>
                        <p>Son las más valiosas e importantes, con consecuencias significativas si no se realizan. <strong>Regla de oro:</strong> Nunca realizar una tarea B o C mientras exista una A pendiente.</p>
                    </div>
                    <div class="abc-card">
                        <span class="abc-badge">B</span>
                        <h3>Tareas "B" - Importancia Media</h3>
                        <p>Son actividades importantes, pero con consecuencias menores en el corto plazo. Se atienden únicamente después de completar las tareas de categoría A.</p>
                    </div>
                    <div class="abc-card">
                        <span class="abc-badge">C</span>
                        <h3>Tareas "C" - Escaso Valor</h3>
                        <p>Actividades de escaso valor o bajo impacto que podrían eliminarse, posponerse o delegarse sin generar un impacto negativo sustancial.</p>
                    </div>
                </div>
            </div>

            <!-- Tracy Comer el Sapo Section -->
            <div class="tracy-card">
                <strong>La Estrategia “Comer el sapo” (Tracy, 2014):</strong> Iniciar siempre la jornada con la tarea más importante y de mayor impacto ("el sapo"), sin importar su dificultad o incomodidad. Dado que la fuerza de voluntad y la concentración son mayores al inicio del día, ejecutar la tarea crítica primero maximiza la efectividad y la calidad del trabajo.
            </div>
        </div>
    </div>

    <!-- Modal Dialog -->
    <div class="modal-overlay" id="modalOverlay" onclick="closeModalOnOuterClick(event)">
        <div class="modal-content">
            <button class="close-btn" onclick="closeModal()">&times;</button>
            <div class="modal-header">
                <div class="modal-title" id="modalTitle">Título</div>
                <div class="modal-subtitle" id="modalSubtitle">Subtítulo</div>
            </div>
            <div class="modal-body" id="modalBody">
                <!-- Dynamic Content -->
            </div>
        </div>
    </div>

    <script>
        const modalData = {
            1: {
                title: "Cuadrante I: Crisis",
                subtitle: "Urgente e Importante",
                description: "Representa actividades que requieren atención inmediata y tienen un alto impacto. Atenderlas es inevitable, pero vivir en este cuadrante genera agotamiento y estrés continuo.",
                examples: [
                    "Proyectos con fechas límite vencidas o inminentes",
                    "Problemas apremiantes y emergencias médicas o técnicas",
                    "Reuniones de crisis o imprevistos de clientes clave"
                ],
                action: "Recomendación: HACER DE INMEDIATO. Buscar reducir este cuadrante mediante una mejor planificación en el Cuadrante II."
            },
            2: {
                title: "Cuadrante II: Planificación",
                subtitle: "Importante, No Urgente",
                description: "Es el cuadrante de la efectividad a largo plazo, la proactividad y el liderazgo personal. Quien lo prioriza reduce progresivamente las crisis del Cuadrante I.",
                examples: [
                    "Planificación estratégica y establecimiento de metas",
                    "Desarrollo de habilidades y capacitación",
                    "Prevención de problemas, mantenimiento y cuidado de salud",
                    "Construcción y fortalecimiento de relaciones interpersonales"
                ],
                action: "Recomendación: PLANIFICAR Y AGENDAR. La estrategia de Covey (2015) consiste en migrar deliberadamente el tiempo hacia este cuadrante."
            },
            3: {
                title: "Cuadrante III: Interrupciones",
                subtitle: "Urgente, No Importante",
                description: "Generan la ilusión de productividad porque requieren respuesta inmediata, pero responden a las prioridades y agendas de otros, no a las metas propias.",
                examples: [
                    "Interrupciones constantes y llamadas no programadas",
                    "Correos electrónicos y mensajes de bajo valor",
                    "Reuniones innecesarias o sin un objetivo claro",
                    "Peticiones secundarias de terceros"
                ],
                action: "Recomendación: DELEGAR O DECIR NO. Minimizar estas actividades para recuperar tiempo efectivo de valor."
            },
            4: {
                title: "Cuadrante IV: Evasión",
                subtitle: "No Urgente, No Importante",
                description: "Actividades de evasión y entretenimiento sin valor agregado. No contribuyen a los objetivos personales ni profesionales y consumen energía de forma pasiva.",
                examples: [
                    "Uso indiscriminado de redes sociales o televisión por evasión",
                    "Navegación web trivial y distracciones de rutina",
                    "Actividades de escape para postergar tareas complejas"
                ],
                action: "Recomendación: ELIMINAR O DESDENTAR. Reducir al mínimo este cuadrante para maximizar el tiempo en el Cuadrante II."
            }
        };

        function openModal(quadrantId) {
            const data = modalData[quadrantId];
            if (!data) return;

            document.getElementById('modalTitle').innerText = data.title;
            document.getElementById('modalSubtitle').innerText = data.subtitle;

            let htmlContent = `<p style="margin-bottom: 12px;">${data.description}</p>`;
            htmlContent += `<div class="modal-section-title">Ejemplos de actividades:</div><ul>`;
            data.examples.forEach(ex => {
                htmlContent += `<li>${ex}</li>`;
            });
            htmlContent += `</ul>`;
            htmlContent += `<div class="action-box">${data.action}</div>`;

            document.getElementById('modalBody').innerHTML = htmlContent;
            document.getElementById('modalOverlay').classList.add('active');
        }

        function closeModal() {
            document.getElementById('modalOverlay').classList.remove('active');
        }

        function closeModalOnOuterClick(event) {
            if (event.target === document.getElementById('modalOverlay')) {
                closeModal();
            }
        }
    </script>
</body>
</html>
"""

with open("3raestrategia.html", "w", encoding="utf-8") as f:
    f.write(htmlContent)

print("HTML file created successfully: 3raestrategia.html")