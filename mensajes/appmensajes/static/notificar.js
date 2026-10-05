document.addEventListener("DOMContentLoaded", () =>{
    const boton = document.getElementById("btn-notificar");
    const estado = document.getElementById("estado-notificacion");
    let count = 1;
    
    boton.addEventListener("click", () => {
        estado.textContent = "Enviando mensaje...";

        const nuevoC = count + 1

        fetch("https://ntfy.sh/nacho-boton-notificacion-directa",{
            method: "POST",
            headers: {
                "X-Title": "Te extrañoooo"
            },
            body: `Estoy pensando en ti x${count}`,
        })
        .then(() => {
            count = nuevoC;
            estado.textContent = "Enviado";
        })
        .catch((error) => {
            estado.textContent = "Error al enviar notificacion";
        });
    });
});
