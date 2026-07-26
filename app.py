from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# BASE DE DATOS REORGANIZADA Y LIMPIA
menu_items = [
    # ---- TANDA 1: BALANCED (Nuevos Platos) ----
    {
        "id": 1, "day": "Lunes", "title": "Coastal Steak Bowl", "category": "Balanced", "active": True,
        "desc": "Savor a succulent, marinated New York Strip steak, grilled to perfection and sliced over a bed of cilantro-lime brown rice.",
        "image": "costal_steak.png"
    },
    {
        "id": 2, "day": "Martes", "title": "Chuleta de Cerdo", "category": "Balanced", "active": True,
        "desc": "Jugosa chuleta de cerdo a la plancha con guarniciones de temporada.",
        "image": "chuleta.png"
    },
    {
        "id": 3, "day": "Miércoles", "title": "Executive Pabellón Moderno", "category": "Balanced", "active": True,
        "desc": "A refined twist on the Venezuelan classic. Slow-shredded flank steak is paired with caramelized plantains.",
        "image": "pabellon.png"
    },
    {
        "id": 4, "day": "Jueves", "title": "Chic Chicken Special", "category": "Balanced", "active": True,
        "desc": "Pollo especial Chic Table preparado con una receta única.",
        "image": "Chic_chicken.png"
    },
    {
        "id": 5, "day": "Viernes", "title": "Quesadilla / Tacos", "category": "Balanced", "active": True,
        "desc": "Queso mozzarella, steak o pollo, cebolla y cilantro. Incluye crema de espinaca y jugo de Jamaica.",
        "image": "quesadilla_taco.png"
    },
    
    # ---- TANDA 2: FITNESS (Platos Originales con la actualización del viernes) ----
    {
        "id": 6, "day": "Lunes", "title": "Lean Power Bowl", "category": "Fitness", "active": False,
        "desc": "A nutrient-dense bowl with fluffy tri-color quinoa, roasted chickpeas and sweet potato.",
        "image": "lean_power.png"
    },
    {
        "id": 7, "day": "Martes", "title": "Chic Chicken Arepa Plate", "category": "Fitness", "active": False,
        "desc": "Indulge in two crisp-fried, artisanal Venezuelan-style arepas stuffed with shredded, slow-cooked chicken.",
        "image": "Chicken_arepa.png"
    },
    {
        "id": 8, "day": "Miércoles", "title": "Turkey Lettuce Tacos", "category": "Fitness", "active": False,
        "desc": "Crisp artisan lettuce cups filled with seasoned, lean ground turkey.",
        "image": "Turkey_lettuce.png"
    },
    {
        "id": 9, "day": "Jueves", "title": "Steak Fit Plate", "category": "Fitness", "active": False,
        "desc": "Enjoy a lean, perfectly seared top sirloin steak served alongside crisp asparagus.",
        "image": "Eteak_fit.png"
    },
    {
        "id": 10, "day": "Viernes", "title": "Shrimp Wellness Bowl", "category": "Fitness", "active": False,
        "desc": "Fresh seasoned grilled shrimp, avocado, cherry tomatoes, corn, black beans, and spinach.",
        "image": "shrimp_wellness.png"
    }
]

# Ruta principal para mostrar el menú activo en la página web
@app.route('/')
def index():
    menu_del_dia = {}
    for plato in menu_items:
        if plato['active']:
            menu_del_dia[plato['day']] = plato
            
    dias_ordenados = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    menu_final = [menu_del_dia[dia] for dia in dias_ordenados if dia in menu_del_dia]
    
    return render_template('index.html', menu=menu_final)

# Panel secreto protegido con la llave de acceso
@app.route('/panel_secreto')
def admin():
    llave = request.args.get('llave', '')
    if llave == 'kelly2026':
        return render_template('admin.html', todos_los_platos=menu_items)
    else:
        return redirect(url_for('index'))

# Función para alternar la tanda activa desde el panel de administración
@app.route('/toggle/<int:plato_id>')
def toggle_plato(plato_id):
    llave = request.args.get('llave', '')
    if llave != 'kelly2026':
        return redirect(url_for('index'))

    plato_seleccionado = next((p for p in menu_items if p['id'] == plato_id), None)
            
    if plato_seleccionado:
        nuevo_estado = not plato_seleccionado['active']
        
        if nuevo_estado == True:
            for p in menu_items:
                if p['day'] == plato_seleccionado['day'] and p['id'] != plato_id:
                    p['active'] = False
                    
        plato_seleccionado['active'] = nuevo_estado

    return redirect(url_for('admin', llave='kelly2026'))

if __name__ == '__main__':
    app.run(debug=True)
