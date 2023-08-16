try {
    document.querySelectorAll('.card-body p').forEach(e => {
        if (e.innerText.includes('Thanks for spending'))
            e.innerText = 'Gracias por pasar un tiempo de calidad con el sitio web hoy.'
    })
} catch (e) {

}
try {
    document.querySelector('footer div.float-right').remove()
} catch (e) {

}