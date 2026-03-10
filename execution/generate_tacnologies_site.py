import os
import sys

# Asegurar que podemos importar utils desde el root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PROJECT_ROOT)

from utils.logger import log_execution

COMMON_HEAD_STYLE = """
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#004A99',
                        accent: '#00A2E0',
                        darkBg: '#0F172A',
                        lightBg: '#F8FAFC'
                    },
                    backgroundImage: {
                        'gradient-modern': 'linear-gradient(135deg, #004A99 0%, #00A2E0 100%)',
                    }
                }
            }
        }
    </script>
    <style>
        body { transition: background-color 0.3s ease, color 0.3s ease; }
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .dark .glass-card {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        @keyframes pulse-glow {
            0%, 100% { filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.6)); }
            50% { filter: drop-shadow(0 0 20px rgba(255, 255, 255, 1)); }
        }
        .logo-glow { animation: pulse-glow 3s infinite; }
        @keyframes gradient-xy {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        .animate-gradient-xy {
            background-size: 200% 200%;
            animation: gradient-xy 12s ease infinite;
        }
        .network-pattern {
            background-image: url("data:image/svg+xml,%3Csvg width='200' height='200' xmlns='http://www.w3.org/2000/svg'%3E%3Cg stroke='rgba(255,255,255,0.15)' stroke-width='1.5' fill='none'%3E%3Cpath d='M30,30 L110,60 L170,30 L140,140 L30,170 Z'/%3E%3Cpath d='M110,60 L140,140 L30,30'/%3E%3Cpath d='M170,30 L30,170'/%3E%3C/g%3E%3Cg fill='rgba(0,162,224,0.6)'%3E%3Ccircle cx='30' cy='30' r='3'/%3E%3Ccircle cx='110' cy='60' r='5'/%3E%3Ccircle cx='170' cy='30' r='3'/%3E%3Ccircle cx='140' cy='140' r='6'/%3E%3Ccircle cx='30' cy='170' r='4'/%3E%3C/g%3E%3Cg fill='rgba(255,0,255,0.5)'%3E%3Ccircle cx='110' cy='60' r='2'/%3E%3Ccircle cx='140' cy='140' r='2'/%3E%3C/g%3E%3C/svg%3E");
            background-size: 250px 250px;
        }
        @keyframes network-drift {
            0% { background-position: 0px 0px; }
            100% { background-position: 250px 250px; }
        }
        .animate-network { animation: network-drift 30s linear infinite; }
        
        .service-tile {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .service-tile:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 15px 30px rgba(0, 162, 224, 0.15);
            border-color: rgba(0, 162, 224, 0.5);
        }
    </style>
"""

TRANSLATION_SCRIPT = """
    <!-- Script de Traducción y Modo Oscuro -->
    <script>
        const translations = {
            "en": {
                "nav_home": "Home",
                "nav_about": "About",
                "nav_services": "Services",
                "nav_contact": "Contact",
                "nav_cta": "Free Consultation",
                
                "hero_empowering": "Empowering Digital",
                "hero_transformation": "Transformation",
                "hero_sub": "Simple, reliable, and secure IT solutions designed for growth.",
                "hero_quote": '"We manage your IT so you can run your business."',
                "hero_btn_services": "Our Services",
                "hero_btn_hours": "Hours",
                "hero_btn_corp": "Corporate Responsibility",
                
                "modal_hours_title": "Business Hours",
                "modal_hours_mo_fr": "Monday: 9:00 AM – 6:00 PM",
                "modal_hours_tu": "Tuesday: 9:00 AM – 6:00 PM",
                "modal_hours_we": "Wednesday: 9:00 AM – 6:00 PM",
                "modal_hours_th": "Thursday: 9:00 AM – 6:00 PM",
                "modal_hours_fr": "Friday: 9:00 AM – 6:00 PM",
                "modal_hours_sa": "Saturday: 10:00 AM – 4:00 PM",
                "modal_hours_su": "Sunday: Closed",
                
                "modal_corp_title": "Our Sustainability & Philanthropy Commitment",
                "modal_corp_p1": "As part of our sustainability commitment, we actively invest in the development of future talent by collaborating with local universities and educational institutions. Through mentorship, internship, and research partnership programs, we aim to empower the next generation of professionals with the skills and knowledge needed to drive innovation in technology and sustainable business practices.",
                "modal_corp_p2": "We also believe in building partnerships with organizations that share our values in promoting non-carbon emission operations and environmental responsibility. By aligning with companies that prioritize green energy, efficient resource management, and planet-friendly innovation, we reinforce our collective mission to reduce environmental impact and contribute to a more sustainable future for all.",
                "modal_corp_p3": "Furthermore, we are committed to upholding diversity, inclusion, and human rights across all aspects of our business. We believe that embracing diverse perspectives and ensuring fair, ethical treatment for all individuals strengthens our company, our communities, and the positive impact we can make on the world.",
                "modal_corp_p4": "Our philanthropic efforts focus on giving back to the communities where we live and work. We support initiatives that promote education, digital inclusion, and social development, believing that technology and compassion together can help build stronger, more equitable societies.",

                "about_title": "About",
                "about_subtitle": "Us",
                "about_p1": "We are a next-generation Managed Security Services Provider (MSSP) and integrator, built on fresh thinking, bold ideas, and a clear mission: to solve your pain points with creative, effective solutions that not only protect your business but elevate your IT operations.",
                "about_p2": "We believe in transparency, clean design, and long-term partnerships built on trust. Whether you’re a startup or an enterprise, we’re here to help you make technology work for you.",
                
                "link_services_title": "Our Expertise at Your Disposal",
                "link_services_btn": "View All Our Services",

                "commitment_title": "Our Commitment",
                "commitment_p": "We don’t just provide technology; we build the future. At Tacnologies, we firmly believe in ethical and sustainable technological development.",
                "commitment_li1": "Local Talent:",
                "commitment_li1_desc": " Continuous investment in exceptional professionals.",
                "commitment_li2": "Sustainability:",
                "commitment_li2_desc": " Operations focused on zero environmental emissions.",
                "commitment_li3": "Diversity:",
                "commitment_li3_desc": " Creating inclusive and plural environments.",

                "contact_title": "Connect With Us",
                "contact_p": "We are ready to transform your infrastructure. Contact us for an initial assessment.",
                "contact_phone": "Phone",
                "contact_email": "Email",
                "contact_web": "Website",

                "hours_title": "Operating Hours",
                "hours_week": "Monday - Friday",
                "hours_sat": "Saturday",
                "hours_sat_val": "Emergency Support",
                "hours_sun": "Sunday",
                "hours_sun_val": "Closed (24/7 Monitoring active)",

                "footer_copy": "© 2026 Tacnologies. All rights reserved.",

                "srv_title": "Our",
                "srv_subtitle": "Services",

                "srv_edr_title": "Endpoint Detection & Response (EDR)",
                "srv_edr_p": "We provide real-time monitoring, threat detection, and automated response across all endpoints in your network. Our EDR solutions identify suspicious behavior, isolate infected devices, and provide actionable insights before threats become breaches.",
                "srv_edr_li1": "24/7 endpoint monitoring",
                "srv_edr_li2": "Threat hunting & behavioral analysis",
                "srv_edr_li3": "Rapid containment & incident response",

                "srv_patch_title": "Patch Management",
                "srv_patch_p": "Outdated software is a key vulnerability. We manage patch cycles across your IT environment to reduce exposure to known exploits, ensuring your systems are always up to date.",
                "srv_patch_li1": "Automated OS and third-party patching",
                "srv_patch_li2": "Patch compliance reporting",
                "srv_patch_li3": "Risk-based patch prioritization",

                "srv_fw_title": "Firewall & Network Security Solutions",
                "srv_fw_p": "We implement and manage firewalls and secure network architectures that protect your critical systems from internal and external threats.",
                "srv_fw_suchas": "such as:",
                "srv_fw_li1": "Next-gen firewall deployment & management",
                "srv_fw_li2": "VPN & remote access configurations",
                "srv_fw_li3": "Network segmentation & intrusion prevention",

                "srv_cloud_title": "Cloud Solutions & Management",
                "srv_cloud_p": "Our experts specialize in Cloud environments — from deployment to optimization and security.",
                "srv_cloud_li1": "Cloud Management & Monitoring (via MOM – Microsoft Operations Manager)",
                "srv_cloud_li2": "Configuration and Policy Management",
                "srv_cloud_li3": "Identity and access management (IAM)",

                "srv_bk_title": "Backup Solutions",
                "srv_bk_p": "Ensure business continuity with reliable and encrypted backup solutions tailored for on-premises and cloud workloads.",
                "srv_bk_li1": "Automated cloud and local backups",
                "srv_bk_li2": "Disaster recovery planning",
                "srv_bk_li3": "Restore testing and backup validation",

                "srv_hyp_li1": "Virtual machine provisioning & management",
                "srv_hyp_li2": "High availability and resource efficiency",

                "form_title": "Contact Us",
                "form_subtitle": "Have a question or project in mind? Let's connect.",
                "form_name_placeholder": "Your Name",
                "form_email_placeholder": "Your Email",
                "form_message_placeholder": "Your Message",
                "form_send_btn": "Send Message"
            },
            "es": {
                "nav_home": "Inicio",
                "nav_about": "Nosotros",
                "nav_services": "Servicios",
                "nav_contact": "Contacto",
                "nav_cta": "Consultoría Gratis",
                
                "hero_empowering": "Empoderando la Transformación",
                "hero_transformation": "Digital",
                "hero_sub": "Soluciones IT simples, confiables y seguras diseñadas para el crecimiento.",
                "hero_quote": '"Gestionamos su IT para que usted pueda dirigir su negocio."',
                "hero_btn_services": "Nuestros Servicios",
                "hero_btn_hours": "Horarios",
                "hero_btn_corp": "Responsabilidad Corporativa",
                
                "modal_hours_title": "Horarios de Atención",
                "modal_hours_mo_fr": "Lunes: 9:00 AM – 6:00 PM",
                "modal_hours_tu": "Martes: 9:00 AM – 6:00 PM",
                "modal_hours_we": "Miércoles: 9:00 AM – 6:00 PM",
                "modal_hours_th": "Jueves: 9:00 AM – 6:00 PM",
                "modal_hours_fr": "Viernes: 9:00 AM – 6:00 PM",
                "modal_hours_sa": "Sábado: 10:00 AM – 4:00 PM",
                "modal_hours_su": "Domingo: Cerrado",
                
                "modal_corp_title": "Nuestro Compromiso con la Sostenibilidad y Filantropía",
                "modal_corp_p1": "Como parte de nuestro compromiso con la sostenibilidad, invertimos activamente en el desarrollo del talento futuro colaborando con universidades e instituciones educativas locales. A través de programas de tutoría, pasantías y asociaciones de investigación, nuestro objetivo es empoderar a la próxima generación de profesionales con las habilidades y el conocimiento necesarios para impulsar la innovación en tecnología y prácticas comerciales sostenibles.",
                "modal_corp_p2": "También creemos en la creación de asociaciones con organizaciones que comparten nuestros valores en la promoción de operaciones sin emisiones de carbono y la responsabilidad ambiental. Al alinearnos con empresas que priorizan la energía verde, la gestión eficiente de los recursos y la innovación respetuosa con el planeta, reforzamos nuestra misión colectiva de reducir el impacto ambiental y contribuir a un futuro más sostenible para todos.",
                "modal_corp_p3": "Además, nos comprometemos a defender la diversidad, la inclusión y los derechos humanos en todos los aspectos de nuestro negocio. Creemos que adoptar perspectivas diversas y garantizar un trato justo y ético para todas las personas fortalece nuestra empresa, nuestras comunidades y el impacto positivo que podemos tener en el mundo.",
                "modal_corp_p4": "Nuestros esfuerzos filantrópicos se centran en retribuir a las comunidades donde vivimos y trabajamos. Apoyamos iniciativas que promueven la educación, la inclusión digital y el desarrollo social, creyendo que la tecnología y la compasión juntas pueden ayudar a construir sociedades más fuertes y equitativas.",

                "about_title": "Sobre",
                "about_subtitle": "Nosotros",
                "about_p1": "Somos un Proveedor de Servicios de Seguridad Gestionados (MSSP) e integrador de próxima generación, construido sobre pensamiento fresco, ideas audaces y una misión clara: resolver sus puntos de dolor con soluciones creativas y efectivas que no solo protegen su negocio, sino que elevan sus operaciones de TI.",
                "about_p2": "Creemos en la transparencia, el diseño limpio y las alianzas a largo plazo construidas sobre la confianza. Ya sea que sea una startup o una empresa, estamos aquí para ayudarlo a hacer que la tecnología trabaje para usted.",
                
                "link_services_title": "Nuestra Experiencia a tu Disposición",
                "link_services_btn": "Ver Todos Nuestros Servicios",

                "commitment_title": "Nuestro Compromiso",
                "commitment_p": "No solo proveemos tecnología; construimos el futuro. En Tacnologies creemos firmemente en un desarrollo tecnológico ético y sostenible.",
                "commitment_li1": "Talento Local:",
                "commitment_li1_desc": " Inversión continua en profesionales excepcionales.",
                "commitment_li2": "Sostenibilidad:",
                "commitment_li2_desc": " Operaciones enfocadas en cero emisiones ambientales.",
                "commitment_li3": "Diversidad:",
                "commitment_li3_desc": " Creación de entornos inclusivos y plurales.",

                "contact_title": "Conecte con Nosotros",
                "contact_p": "Estamos listos para transformar su infraestructura. Contáctenos para una evaluación inicial.",
                "contact_phone": "Teléfono",
                "contact_email": "Email",
                "contact_web": "Página Web",

                "hours_title": "Horarios de Operación",
                "hours_week": "Lunes - Viernes",
                "hours_sat": "Sábado",
                "hours_sat_val": "Soporte de Emergencia",
                "hours_sun": "Domingo",
                "hours_sun_val": "Cerrado (Monitoreo 24/7 activo)",

                "footer_copy": "© 2026 Tacnologies. Todos los derechos reservados.",

                "srv_title": "Nuestros",
                "srv_subtitle": "Servicios",

                "srv_edr_title": "Endpoint Detection & Response (EDR)",
                "srv_edr_p": "Proporcionamos monitoreo en tiempo real, detección de amenazas y respuesta automatizada en todos los endpoints de su red. Nuestras soluciones EDR identifican comportamientos sospechosos, aíslan dispositivos infectados y brindan información procesable antes de que las amenazas se conviertan en brechas.",
                "srv_edr_li1": "Monitoreo de endpoints 24/7",
                "srv_edr_li2": "Caza de amenazas y análisis de comportamiento",
                "srv_edr_li3": "Contención rápida y respuesta a incidentes",

                "srv_patch_title": "Gestión de Parches (Patch Management)",
                "srv_patch_p": "El software desactualizado es una vulnerabilidad clave. Gestionamos ciclos de parches en su entorno de TI para reducir la exposición a exploits conocidos, asegurando que sus sistemas estén siempre actualizados.",
                "srv_patch_li1": "Parcheo automatizado de SO y terceros",
                "srv_patch_li2": "Informes de cumplimiento de parches",
                "srv_patch_li3": "Priorización de parches basada en riesgos",

                "srv_fw_title": "Soluciones de Firewall y Seguridad de Red",
                "srv_fw_p": "Implementamos y gestionamos firewalls y arquitecturas de red seguras que protegen sus sistemas críticos de amenazas internas y externas.",
                "srv_fw_suchas": "tales como:",
                "srv_fw_li1": "Despliegue y gestión de firewalls de próxima generación",
                "srv_fw_li2": "Configuraciones de VPN y acceso remoto",
                "srv_fw_li3": "Segmentación de red y prevención de intrusiones",

                "srv_cloud_title": "Soluciones y Gestión Cloud",
                "srv_cloud_p": "Nuestros expertos se especializan en entornos Cloud — desde el despliegue hasta la optimización y seguridad.",
                "srv_cloud_li1": "Gestión y Monitoreo Cloud (vía MOM – Microsoft Operations Manager)",
                "srv_cloud_li2": "Gestión de Políticas y Configuración",
                "srv_cloud_li3": "Gestión de identidad y accesos (IAM)",

                "srv_bk_title": "Soluciones de Backup",
                "srv_bk_p": "Garantice la continuidad del negocio con soluciones de respaldo confiables y encriptadas adaptadas para cargas de trabajo locales y en la nube.",
                "srv_bk_li1": "Respaldos automatizados locales y en la nube",
                "srv_bk_li2": "Planificación de recuperación ante desastres",
                "srv_bk_li3": "Pruebas de restauración y validación de respaldos",

                "srv_hyp_li1": "Aprovisionamiento y gestión de máquinas virtuales",
                "srv_hyp_li2": "Alta disponibilidad y eficiencia de recursos",

                "form_title": "Contacto",
                "form_subtitle": "¿Tiene una pregunta o un proyecto en mente? Conectemos.",
                "form_name_placeholder": "Su Nombre",
                "form_email_placeholder": "Su Email",
                "form_message_placeholder": "Su Mensaje",
                "form_send_btn": "Enviar Mensaje"
            }
        };

        const langBtn = document.getElementById('lang-toggle');
        const langText = document.getElementById('lang-text');

        function setLanguage(lang) {
            localStorage.setItem('sys-lang', lang);
            langText.innerText = lang.toUpperCase();
            
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                        el.placeholder = translations[lang][key];
                    } else {
                        el.innerHTML = translations[lang][key];
                    }
                }
            });

            // Update Document Language
            document.documentElement.lang = lang;
        }

        langBtn.addEventListener('click', () => {
            const currentLang = localStorage.getItem('sys-lang') || 'en';
            setLanguage(currentLang === 'en' ? 'es' : 'en');
        });

        // Handlers para abrir/cerrar Modals
        function openModal(id) {
            document.getElementById(id).classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }
        function closeModal(id) {
            document.getElementById(id).classList.add('hidden');
            document.body.style.overflow = '';
        }

        // Cerrar si se hace click fuera del modal
        window.addEventListener('click', function(e) {
            if (e.target.classList.contains('bg-black/80')) {
                e.target.classList.add('hidden');
                document.body.style.overflow = '';
            }
        });

        // Modo Oscuro
        const themeToggleBtn = document.getElementById('theme-toggle');
        const darkIcon = document.getElementById('theme-icon-dark');
        const lightIcon = document.getElementById('theme-icon-light');

        function toggleTheme() {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
                darkIcon.classList.remove('hidden');
                lightIcon.classList.add('hidden');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
                darkIcon.classList.add('hidden');
                lightIcon.classList.remove('hidden');
            }
        }

        // Setup inicial
        const savedLang = localStorage.getItem('sys-lang') || 'en';
        setLanguage(savedLang);

        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
            darkIcon.classList.add('hidden');
            lightIcon.classList.remove('hidden');
        } else {
            document.documentElement.classList.remove('dark');
            darkIcon.classList.remove('hidden');
            lightIcon.classList.add('hidden');
        }

        themeToggleBtn.addEventListener('click', toggleTheme);
    </script>
</body>
</html>
"""

NAV_HTML = """
    <!-- Navegación -->
    <nav class="fixed w-full z-50 top-0 transition-all duration-300 bg-white/80 dark:bg-darkBg/80 backdrop-blur-md border-b border-gray-200 dark:border-white/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <a href="index.html" class="flex-shrink-0 flex items-center">
                    <img class="h-10 w-auto logo-glow" src="https://d16y57bdjt0bnh.cloudfront.net/customerwebpages/tacnologies-assets/tacnologieslogo.png" alt="Tacnologies Logo" id="nav-logo" onerror="this.src='https://initiumtech.s3.us-east-1.amazonaws.com/customerwebpages/tacnologies-assets/tacnologieslogo.png'">
                    <span class="ml-3 text-xl font-bold text-primary dark:text-white">TACNOLOGIES</span>
                </a>
                
                <!-- Menú Desktop -->
                <div class="hidden md:flex items-center space-x-6">
                    <a href="index.html" data-i18n="nav_home" class="text-sm font-medium hover:text-accent transition-colors">Home</a>
                    <a href="index.html#about" data-i18n="nav_about" class="text-sm font-medium hover:text-accent transition-colors">About</a>
                    <a href="services.html" data-i18n="nav_services" class="text-sm font-medium text-accent hover:text-primary transition-colors">Services</a>
                    <a href="index.html#contacto" data-i18n="nav_contact" class="text-sm font-medium hover:text-accent transition-colors">Contact</a>
                    
                    <div class="flex items-center space-x-2 border-l border-gray-300 dark:border-white/10 pl-4 ml-2">
                        <!-- Botón Idioma -->
                        <button id="lang-toggle" class="px-3 py-1.5 rounded bg-gray-200 dark:bg-slate-800 text-gray-700 dark:text-accent hover:bg-gray-300 dark:hover:bg-slate-700 transition-colors focus:outline-none flex items-center shadow shadow-black/10">
                            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"></path></svg>
                            <span id="lang-text" class="text-xs font-bold font-mono">EN</span>
                        </button>
                    
                        <!-- Botón Modo Oscuro/Claro -->
                        <button id="theme-toggle" class="p-2 mr-4 rounded bg-gray-200 dark:bg-slate-800 text-gray-600 dark:text-accent hover:bg-gray-300 dark:hover:bg-slate-700 transition-colors focus:outline-none shadow shadow-black/10">
                            <svg id="theme-icon-light" class="w-4 h-4 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                            <svg id="theme-icon-dark" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                        </button>
                    </div>
                    
                    <a href="index.html#contacto" data-i18n="nav_cta" class="bg-gradient-modern text-white px-6 py-2 rounded-full font-semibold shadow-lg hover:shadow-accent/50 transition-all duration-300 transform hover:-translate-y-0.5">
                        Free Consultation
                    </a>
                </div>
            </div>
        </div>
    </nav>
"""

FOOTER_HTML = """
    <!-- Seccion Contacto (Formulario y Detalles) -->
    <section id="contacto" class="py-20 bg-slate-50 dark:bg-[#111111]">
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-10">
                <h2 data-i18n="form_title" class="text-3xl font-bold text-accent mb-4">Contact Us</h2>
                <p data-i18n="form_subtitle" class="text-slate-600 dark:text-gray-300">Have a question or project in mind? Let's connect.</p>
            </div>
            <form class="space-y-4">
                <div>
                    <input type="text" data-i18n="form_name_placeholder" placeholder="Your Name" class="w-full px-4 py-3 rounded-lg bg-white text-slate-900 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent dark:border-none">
                </div>
                <div>
                    <input type="email" data-i18n="form_email_placeholder" placeholder="Your Email" class="w-full px-4 py-3 rounded-lg bg-white text-slate-900 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent dark:border-none">
                </div>
                <div>
                    <textarea data-i18n="form_message_placeholder" placeholder="Your Message" rows="5" class="w-full px-4 py-3 rounded-lg bg-white text-slate-900 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent dark:border-none"></textarea>
                </div>
                <div>
                    <button type="button" class="bg-white text-accent font-bold py-3 px-8 rounded-full shadow-md hover:bg-gray-100 transition-colors inline-block mt-2">
                        <span data-i18n="form_send_btn">Send Message</span>
                    </button>
                </div>
            </form>
        </div>
    </section>

    <!-- Horarios y Contacto Info -->
    <section class="py-20 bg-white dark:bg-[#0B1120] border-t border-gray-100 dark:border-white/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-16 items-center">
                <div>
                    <h2 data-i18n="contact_title" class="text-3xl font-bold mb-6 text-slate-900 dark:text-white">Connect With Us</h2>
                    <p data-i18n="contact_p" class="text-slate-600 dark:text-gray-400 mb-10 max-w-md">
                        We are ready to transform your infrastructure. Contact us for an initial assessment.
                    </p>
                    <div class="space-y-6">
                        <div class="flex items-center">
                            <svg class="w-5 h-5 text-accent mr-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                            <div>
                                <p data-i18n="contact_phone" class="text-xs text-slate-500 dark:text-gray-500">Phone</p>
                                <a href="tel:7875086578" class="text-base font-semibold text-slate-900 dark:text-white hover:text-accent transition-colors">787-508-6578</a>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <svg class="w-5 h-5 text-accent mr-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            <div>
                                <p data-i18n="contact_email" class="text-xs text-slate-500 dark:text-gray-500">Email</p>
                                <a href="mailto:info@tacnologies.com" class="text-base font-semibold text-slate-900 dark:text-white hover:text-accent transition-colors">info@tacnologies.com</a>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <svg class="w-5 h-5 text-accent mr-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
                            <div>
                                <p data-i18n="contact_web" class="text-xs text-slate-500 dark:text-gray-500">Website</p>
                                <a href="http://www.tacnologies.com" target="_blank" class="text-base font-semibold text-slate-900 dark:text-white hover:text-accent transition-colors">www.tacnologies.com</a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="bg-slate-50 dark:bg-[#1E293B] rounded-3xl p-8 border border-gray-100 dark:border-white/5 shadow-2xl">
                    <h3 data-i18n="hours_title" class="text-lg font-bold mb-6 text-slate-900 dark:text-white">Operating Hours</h3>
                    <ul class="space-y-4 text-sm text-slate-600 dark:text-gray-400">
                        <li class="flex justify-between border-b border-gray-200 dark:border-white/10 pb-3">
                            <span data-i18n="hours_week">Monday - Friday</span>
                            <span class="font-medium text-slate-900 dark:text-white">8:00 AM - 6:00 PM</span>
                        </li>
                        <li class="flex justify-between border-b border-gray-200 dark:border-white/10 pb-3">
                            <span data-i18n="hours_sat">Saturday</span>
                            <span data-i18n="hours_sat_val" class="font-medium text-slate-900 dark:text-white">Emergency Support</span>
                        </li>
                        <li class="flex justify-between pb-1">
                            <span data-i18n="hours_sun">Sunday</span>
                            <span data-i18n="hours_sun_val" class="font-medium text-accent">Closed (24/7 Monitoring active)</span>
                        </li>
                    </ul>
                    <div class="mt-8 pt-6 border-t border-gray-200 dark:border-white/10 text-center">
                        <p data-i18n="footer_copy" class="text-xs text-slate-500">&copy; 2024 Tacnologies. All rights reserved.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

INDEX_HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tacnologies | Managed IT & Technology Services</title>
    {COMMON_HEAD_STYLE}
</head>
<body class="bg-lightBg dark:bg-darkBg text-slate-800 dark:text-slate-200 font-sans antialiased selection:bg-accent selection:text-white">

    {NAV_HTML}

    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden bg-gradient-to-br from-slate-900 via-[#1E3A8A] to-[#8B008B] animate-gradient-xy">
        <div class="absolute inset-0 network-pattern animate-network opacity-60 mix-blend-screen transition-opacity duration-500"></div>
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full max-w-7xl pointer-events-none">
            <div class="absolute top-1/4 right-1/4 w-[30rem] h-[30rem] bg-accent/20 rounded-full blur-[120px] animate-pulse" style="animation-duration: 6s;"></div>
            <div class="absolute bottom-1/4 left-1/4 w-[30rem] h-[30rem] bg-fuchsia-500/20 rounded-full blur-[120px] animate-pulse" style="animation-duration: 4s;"></div>
        </div>
        
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center z-10">
            <h1 class="text-4xl md:text-6xl lg:text-7xl font-extrabold tracking-tight mb-6 drop-shadow-xl border-t border-t-white/10 pt-8" style="border-top: 2px solid rgba(255,255,255,0.05);">
                <span data-i18n="hero_empowering" class="block text-white">Empowering Digital</span>
                <span data-i18n="hero_transformation" class="block text-transparent bg-clip-text bg-gradient-to-r from-accent to-[#FF00FF]">Transformation</span>
            </h1>
            <p class="mt-8 max-w-3xl text-lg md:text-xl mx-auto text-slate-300 font-light mb-10 leading-relaxed border-b border-b-white/10 pb-8" style="border-bottom: 2px solid rgba(255,255,255,0.05);">
                <span data-i18n="hero_sub">Simple, reliable, and secure IT solutions designed for growth.</span> <br class="hidden md:block mt-2"/>
                <strong data-i18n="hero_quote" class="text-white font-medium tracking-wide">"We manage your IT so you can run your business."</strong>
            </p>
            <div class="flex flex-wrap justify-center gap-4 mt-8">
                <a href="services.html" data-i18n="hero_btn_services" class="bg-white text-accent px-6 sm:px-8 py-3 rounded-full font-bold shadow-md hover:shadow-lg transition-all duration-300">
                    Our Services
                </a>
                <button type="button" onclick="openModal('hoursModal')" data-i18n="hero_btn_hours" class="bg-white text-accent px-6 sm:px-8 py-3 rounded-full font-bold shadow-md hover:shadow-lg transition-all duration-300">
                    Hours
                </button>
                <button type="button" onclick="openModal('corpModal')" data-i18n="hero_btn_corp" class="bg-white text-accent px-6 sm:px-8 py-3 rounded-full font-bold shadow-md hover:shadow-lg transition-all duration-300">
                    Corporate Responsibility
                </button>
            </div>
        </div>
        
        <div class="absolute bottom-0 left-0 w-full h-[3px] bg-gradient-to-r from-accent via-fuchsia-500 to-accent"></div>
        <div class="absolute top-0 left-0 w-full h-[3px] bg-gradient-to-r from-accent via-fuchsia-500 to-accent"></div>
    </section>

    <!-- About Us Section -->
    <section id="about" class="py-20 bg-slate-50 dark:bg-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-12 items-center">
                <!-- Imagen -->
                <div class="relative rounded-2xl overflow-hidden shadow-2xl group">
                    <img src="https://d16y57bdjt0bnh.cloudfront.net/customerwebpages/tacnologies-assets/tactecnologies_image1.png" alt="Tacnologies overview" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-700" onerror="this.src='https://initiumtech.s3.us-east-1.amazonaws.com/customerwebpages/tacnologies-assets/tactecnologies_image1.png'">
                    <div class="absolute inset-0 bg-gradient-to-t from-[#8B008B]/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                </div>
                <!-- Contenido -->
                <div>
                    <h2 class="text-3xl font-bold text-slate-900 dark:text-white uppercase tracking-wider mb-6 text-left">
                        <span data-i18n="about_title">About</span> <span data-i18n="about_subtitle" class="text-accent">Us</span>
                    </h2>
                    <div class="w-24 h-1 bg-gradient-modern mt-2 mb-8 rounded-full"></div>
                    <p data-i18n="about_p1" class="text-lg text-slate-600 dark:text-slate-300 mb-6 leading-relaxed">
                        We are a next-generation Managed Security Services Provider (MSSP) and integrator, built on fresh thinking, bold ideas, and a clear mission: to solve your pain points with creative, effective solutions that not only protect your business but elevate your IT operations.
                    </p>
                    <p data-i18n="about_p2" class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
                        We believe in transparency, clean design, and long-term partnerships built on trust. Whether you’re a startup or an enterprise, we’re here to help you make technology work for you.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Enlace a Servicios -->
    <section class="py-16 bg-white dark:bg-slate-900/50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 data-i18n="link_services_title" class="text-2xl font-bold text-slate-900 dark:text-white mb-6">Our Expertise at Your Disposal</h2>
            <a href="services.html" class="inline-flex items-center text-accent hover:text-primary font-bold text-lg transition-colors group">
                <span data-i18n="link_services_btn">View All Our Services</span>
                <svg class="w-5 h-5 ml-2 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </a>
        </div>
    </section>

    <!-- Compromiso Corporativo -->
    <section id="compromiso" class="py-20 relative overflow-hidden backdrop-blur-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-gradient-to-r from-primary to-accent rounded-3xl p-10 md:p-16 text-white shadow-2xl">
                <div class="grid md:grid-cols-2 gap-12 items-center">
                    <div>
                        <h2 data-i18n="commitment_title" class="text-3xl font-bold mb-6">Our Commitment</h2>
                        <p data-i18n="commitment_p" class="text-lg text-white/90 mb-6 font-light leading-relaxed">
                            We don’t just provide technology; we build the future. At Tacnologies, we firmly believe in ethical and sustainable technological development.
                        </p>
                        <ul class="space-y-4">
                            <li class="flex items-center">
                                <span class="w-2 h-2 bg-white rounded-full mr-3"></span>
                                <div><strong data-i18n="commitment_li1">Local Talent:</strong><span data-i18n="commitment_li1_desc"> Continuous investment in exceptional professionals.</span></div>
                            </li>
                            <li class="flex items-center">
                                <span class="w-2 h-2 bg-white rounded-full mr-3"></span>
                                <div><strong data-i18n="commitment_li2">Sustainability:</strong><span data-i18n="commitment_li2_desc"> Operations focused on zero environmental emissions.</span></div>
                            </li>
                            <li class="flex items-center">
                                <span class="w-2 h-2 bg-white rounded-full mr-3"></span>
                                <div><strong data-i18n="commitment_li3">Diversity:</strong><span data-i18n="commitment_li3_desc"> Creating inclusive and plural environments.</span></div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Modals -->
    <!-- Hours Modal -->
    <div id="hoursModal" class="fixed inset-0 bg-black/80 z-50 hidden flex items-center justify-center p-4">
        <div class="bg-[#1A1A1A] rounded-2xl w-full max-w-sm relative p-8 border border-white/10 shadow-2xl">
            <button onclick="closeModal('hoursModal')" class="absolute top-4 right-4 text-gray-400 hover:text-white transition-colors">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <h3 data-i18n="modal_hours_title" class="text-2xl font-bold text-accent mb-6 text-center">Business Hours</h3>
            <ul class="space-y-3 text-white text-center font-medium">
                <li data-i18n="modal_hours_mo_fr">Monday: 9:00 AM – 6:00 PM</li>
                <li data-i18n="modal_hours_tu">Tuesday: 9:00 AM – 6:00 PM</li>
                <li data-i18n="modal_hours_we">Wednesday: 9:00 AM – 6:00 PM</li>
                <li data-i18n="modal_hours_th">Thursday: 9:00 AM – 6:00 PM</li>
                <li data-i18n="modal_hours_fr">Friday: 9:00 AM – 6:00 PM</li>
                <li data-i18n="modal_hours_sa">Saturday: 10:00 AM – 4:00 PM</li>
                <li data-i18n="modal_hours_su">Sunday: Closed</li>
            </ul>
        </div>
    </div>

    <!-- Corporate Responsibility Modal -->
    <div id="corpModal" class="fixed inset-0 bg-black/80 z-50 hidden flex items-center justify-center p-4">
        <div class="bg-[#1A1A1A] rounded-2xl w-full max-w-3xl relative p-8 border border-white/10 shadow-2xl max-h-[90vh] overflow-y-auto">
            <button onclick="closeModal('corpModal')" class="absolute top-4 right-4 text-gray-400 hover:text-white transition-colors">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <h3 data-i18n="modal_corp_title" class="text-2xl font-bold text-accent mb-6">Our Sustainability & Philanthropy Commitment</h3>
            <div class="space-y-4 text-gray-300 leading-relaxed">
                <p data-i18n="modal_corp_p1">As part of our sustainability commitment, we actively invest in the development of future talent by collaborating with local universities and educational institutions. Through mentorship, internship, and research partnership programs, we aim to empower the next generation of professionals with the skills and knowledge needed to drive innovation in technology and sustainable business practices.</p>
                <p data-i18n="modal_corp_p2">We also believe in building partnerships with organizations that share our values in promoting non-carbon emission operations and environmental responsibility. By aligning with companies that prioritize green energy, efficient resource management, and planet-friendly innovation, we reinforce our collective mission to reduce environmental impact and contribute to a more sustainable future for all.</p>
                <p data-i18n="modal_corp_p3">Furthermore, we are committed to upholding diversity, inclusion, and human rights across all aspects of our business. We believe that embracing diverse perspectives and ensuring fair, ethical treatment for all individuals strengthens our company, our communities, and the positive impact we can make on the world.</p>
                <p data-i18n="modal_corp_p4">Our philanthropic efforts focus on giving back to the communities where we live and work. We support initiatives that promote education, digital inclusion, and social development, believing that technology and compassion together can help build stronger, more equitable societies.</p>
            </div>
        </div>
    </div>

{FOOTER_HTML}
{TRANSLATION_SCRIPT}
"""

SERVICES_HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Services | Tacnologies</title>
    {COMMON_HEAD_STYLE}
</head>
<body class="bg-lightBg dark:bg-darkBg text-slate-800 dark:text-slate-200 font-sans antialiased selection:bg-accent selection:text-white">

    {NAV_HTML}

    <!-- Encabezado de la página de Servicios -->
    <div class="pt-32 pb-10 text-center">
        <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-slate-900 dark:text-white">
            <span data-i18n="srv_title">Our</span> <span data-i18n="srv_subtitle" class="text-accent">Services</span>
        </h1>
        <div class="w-24 h-1 bg-gradient-modern mx-auto mt-4 rounded-full"></div>
    </div>

    <!-- Imagen de Datacenter -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 rounded-3xl overflow-hidden shadow-2xl">
        <img src="https://d16y57bdjt0bnh.cloudfront.net/customerwebpages/tacnologies-assets/tacnologiesdatacenterimage.png" alt="Tacnologies Datacenter" class="w-full h-[400px] md:h-[500px] object-cover" onerror="this.src='https://initiumtech.s3.us-east-1.amazonaws.com/customerwebpages/tacnologies-assets/tacnologiesdatacenterimage.png'">
    </div>

    <!-- Grid de Servicios tipo Tile -->
    <section class="py-10 pb-24">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-8">
                
                <!-- Tile 1 EDR -->
                <div class="service-tile p-8 rounded-3xl flex flex-col h-full bg-white dark:bg-[#0B1121] border-2 border-slate-300 dark:border-slate-600 shadow-xl dark:shadow-2xl hover:shadow-2xl hover:border-accent dark:hover:border-accent hover:-translate-y-2 transition-all duration-300">
                    <h3 data-i18n="srv_edr_title" class="text-xl font-bold mb-3 text-slate-900 dark:text-white">Endpoint Detection & Response (EDR)</h3>
                    <p data-i18n="srv_edr_p" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-light mb-4 flex-grow">
                        We provide real-time monitoring, threat detection, and automated response across all endpoints in your network.
                        Our EDR solutions identify suspicious behavior, isolate infected devices, and provide actionable insights
                        before threats become breaches.
                    </p>
                    <ul class="space-y-2 text-sm md:text-base mt-4">
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_edr_li1" class="text-slate-600 dark:text-slate-300">24/7 endpoint monitoring</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_edr_li2" class="text-slate-600 dark:text-slate-300">Threat hunting & behavioral analysis</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_edr_li3" class="text-slate-600 dark:text-slate-300">Rapid containment & incident response</span>
                        </li>
                    </ul>
                </div>

                <!-- Tile 2 Patch -->
                <div class="service-tile p-8 rounded-3xl flex flex-col h-full bg-white dark:bg-[#0B1121] border-2 border-slate-300 dark:border-slate-600 shadow-xl dark:shadow-2xl hover:shadow-2xl hover:border-accent dark:hover:border-accent hover:-translate-y-2 transition-all duration-300">
                    <h3 data-i18n="srv_patch_title" class="text-xl font-bold mb-3 text-slate-900 dark:text-white">Patch Management</h3>
                    <p data-i18n="srv_patch_p" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-light mb-4 flex-grow">
                        Outdated software is a key vulnerability. We manage patch cycles across your IT environment to reduce exposure to known exploits, ensuring your systems are always up to date.
                    </p>
                    <ul class="space-y-2 text-sm md:text-base mt-4">
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_patch_li1" class="text-slate-600 dark:text-slate-300">Automated OS and third-party patching</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_patch_li2" class="text-slate-600 dark:text-slate-300">Patch compliance reporting</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_patch_li3" class="text-slate-600 dark:text-slate-300">Risk-based patch prioritization</span>
                        </li>
                    </ul>
                </div>

                <!-- Tile 3 Firewall -->
                <div class="service-tile p-8 rounded-3xl flex flex-col h-full bg-white dark:bg-[#0B1121] border-2 border-slate-300 dark:border-slate-600 shadow-xl dark:shadow-2xl hover:shadow-2xl hover:border-accent dark:hover:border-accent hover:-translate-y-2 transition-all duration-300">
                    <h3 data-i18n="srv_fw_title" class="text-xl font-bold mb-3 text-slate-900 dark:text-white">Firewall & Network Security Solutions</h3>
                    <p data-i18n="srv_fw_p" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-light mb-4 flex-grow">
                        We implement and manage firewalls and secure network architectures that protect your critical systems from internal and external threats.
                    </p>
                    <p data-i18n="srv_fw_suchas" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-medium mb-2">such as:</p>
                    <ul class="space-y-2 text-sm md:text-base mt-2">
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_fw_li1" class="text-slate-600 dark:text-slate-300">Next-gen firewall deployment & management</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_fw_li2" class="text-slate-600 dark:text-slate-300">VPN & remote access configurations</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_fw_li3" class="text-slate-600 dark:text-slate-300">Network segmentation & intrusion prevention</span>
                        </li>
                    </ul>
                </div>

                <!-- Tile 4 Cloud -->
                <div class="service-tile p-8 rounded-3xl flex flex-col h-full bg-white dark:bg-[#0B1121] border-2 border-slate-300 dark:border-slate-600 shadow-xl dark:shadow-2xl hover:shadow-2xl hover:border-accent dark:hover:border-accent hover:-translate-y-2 transition-all duration-300">
                    <h3 data-i18n="srv_cloud_title" class="text-xl font-bold mb-3 text-slate-900 dark:text-white">Cloud Solutions & Management</h3>
                    <p data-i18n="srv_cloud_p" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-light mb-4 flex-grow">
                        Our experts specialize in Cloud environments — from deployment to optimization and security.
                    </p>
                    <ul class="space-y-2 text-sm md:text-base mt-6">
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_cloud_li1" class="text-slate-600 dark:text-slate-300">Cloud Management & Monitoring (via MOM – Microsoft Operations Manager)</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_cloud_li2" class="text-slate-600 dark:text-slate-300">Configuration and Policy Management</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_cloud_li3" class="text-slate-600 dark:text-slate-300">Identity and access management (IAM)</span>
                        </li>
                    </ul>
                </div>

                <!-- Tile 5 Backup -->
                <div class="service-tile p-8 rounded-3xl flex flex-col h-full bg-white dark:bg-[#0B1121] border-2 border-slate-300 dark:border-slate-600 shadow-xl dark:shadow-2xl hover:shadow-2xl hover:border-accent dark:hover:border-accent hover:-translate-y-2 transition-all duration-300">
                    <h3 data-i18n="srv_bk_title" class="text-xl font-bold mb-3 text-slate-900 dark:text-white">Backup Solutions</h3>
                    <p data-i18n="srv_bk_p" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-light mb-4 flex-grow">
                        Ensure business continuity with reliable and encrypted backup solutions tailored for on-premises and cloud workloads.
                    </p>
                    <ul class="space-y-2 text-sm md:text-base mt-2">
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_bk_li1" class="text-slate-600 dark:text-slate-300">Automated cloud and local backups</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_bk_li2" class="text-slate-600 dark:text-slate-300">Disaster recovery planning</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_bk_li3" class="text-slate-600 dark:text-slate-300">Restore testing and backup validation</span>
                        </li>
                    </ul>
                </div>

                <!-- Tile 6 Hyp -->
                <div class="service-tile p-8 rounded-3xl flex flex-col h-full bg-white dark:bg-[#0B1121] border-2 border-slate-300 dark:border-slate-600 shadow-xl dark:shadow-2xl hover:shadow-2xl hover:border-accent dark:hover:border-accent hover:-translate-y-2 transition-all duration-300">
                    <h3 data-i18n="srv_hyp_title" class="text-xl font-bold mb-3 text-slate-900 dark:text-white">Hypervisor Solutions</h3>
                    <p data-i18n="srv_hyp_p" class="text-sm md:text-base text-slate-600 dark:text-slate-300 font-light mb-4 flex-grow">
                        Ensure business continuity with reliable and encrypted backup solutions tailored for on-premises and cloud workloads.
                    </p>
                    <ul class="space-y-2 text-sm md:text-base mt-2">
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_hyp_li1" class="text-slate-600 dark:text-slate-300">Virtual machine provisioning & management</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-accent mr-2 font-bold">•</span>
                            <span data-i18n="srv_hyp_li2" class="text-slate-600 dark:text-slate-300">High availability and resource efficiency</span>
                        </li>
                    </ul>
                </div>

            </div>
        </div>
    </section>

{FOOTER_HTML}
{TRANSLATION_SCRIPT}
"""

@log_execution
def generate_tacnologies_site():
    """ Genera el archivo index.html y services.html de Tacnologies. """
    index_path = os.path.join(PROJECT_ROOT, 'index.html')
    services_path = os.path.join(PROJECT_ROOT, 'services.html')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(INDEX_HTML_CONTENT)
        
    with open(services_path, 'w', encoding='utf-8') as f:
        f.write(SERVICES_HTML_CONTENT)
        
    print(f"[{__name__}] Landing generada en: {index_path}")
    print(f"[{__name__}] Servicios generados en: {services_path}")
    return {"index": index_path, "services": services_path}

if __name__ == "__main__":
    result = generate_tacnologies_site()
    print("Ejecución del script completada.")
