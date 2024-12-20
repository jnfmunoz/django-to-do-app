// $(document).ready(function(){

//     if(document.body.classList.contains('task-update-page')) {
//         document.getElementById('confirmUpdateBtn').addEventListener('click', function(e){
//             e.preventDefault();
//             Swal.fire({
//                 title: "Actualizar Tarea",
//                 text: "¿Estás seguro de que deseas actualizar esta tarea?",
//                 icon: "question",
//                 showCancelButton: true,
//                 confirmButtonColor: "#3085d6",
//                 cancelButtonColor: "#d33",
//                 confirmButtonText: "Sí, actualizar",
//                 cancelButtonText: "Cancelar"
//             }).then((result) => {
//                 if (result.isConfirmed) {                           
//                     document.getElementById('taskUpdateForm').submit();                
//                 }
//             });            
//         });
//     };

//     if(document.body.classList.contains('task-create-page')) {
//         document.getElementById('confirmCreateBtn').addEventListener('click', function(e){
//             e.preventDefault();
//             Swal.fire({
//                 title: "Agregar Tarea",
//                 text: "¿Estás seguro de que deseas agregar esta tarea?",
//                 icon: "question",
//                 showCancelButton: true,
//                 confirmButtonColor: "#3085d6",
//                 cancelButtonColor: "#d33",
//                 confirmButtonText: "Sí, agregar",
//                 cancelButtonText: "Cancelar"
//             }).then((result) => {
//                 if (result.isConfirmed) {                           
//                     document.getElementById('taskCreateForm').submit();                
//                 }
//             });
//         });
//     };

    
//     if(document.body.classList.contains('task-list-page')) {
//         // Seleccionar todos los botones de eliminación
//         const deleteButtons = document.querySelectorAll('.deleteTaskBtn');

//         // Agregar evento de clic a cada botón de eliminación
//         deleteButtons.forEach(button => {
//             button.addEventListener('click', function(e) {
//                 e.preventDefault(); // Evitar el comportamiento por defecto del botón
                
//                 // Obtener la URL del atributo data-url del botón clicado
//                 const deleteUrl = this.getAttribute('data-url');
                
//                 // Mostrar la alerta de confirmación con SweetAlert
//                 Swal.fire({
//                     title: "Eliminar Tarea",
//                     text: "¿Estás seguro de que deseas eliminar esta tarea?",
//                     icon: "warning",
//                     showCancelButton: true,
//                     confirmButtonColor: "#d33",
//                     cancelButtonColor: "#3085d6",
//                     confirmButtonText: "Sí, eliminar",
//                     cancelButtonText: "Cancelar"
//                 }).then((result) => {
//                     if (result.isConfirmed) {
//                         // Redirigir a la URL de eliminación si el usuario confirma
//                         window.location.href = deleteUrl;
//                     }
//                 });
//             });
//         });
//     };

//     if(document.body.classList.contains('task-detail-page')) {
//         // Seleccionar todos los botones de eliminación
//         const deleteButtons = document.querySelectorAll('.deleteTaskBtn');

//         // Agregar evento de clic a cada botón de eliminación
//         deleteButtons.forEach(button => {
//             button.addEventListener('click', function(e) {
//                 e.preventDefault(); // Evitar el comportamiento por defecto del botón
                
//                 // Obtener la URL del atributo data-url del botón clicado
//                 const deleteUrl = this.getAttribute('data-url');
                
//                 // Mostrar la alerta de confirmación con SweetAlert
//                 Swal.fire({
//                     title: "Eliminar Tarea",
//                     text: "¿Estás seguro de que deseas eliminar esta tarea?",
//                     icon: "warning",
//                     showCancelButton: true,
//                     confirmButtonColor: "#d33",
//                     cancelButtonColor: "#3085d6",
//                     confirmButtonText: "Sí, eliminar",
//                     cancelButtonText: "Cancelar"
//                 }).then((result) => {
//                     if (result.isConfirmed) {
//                         // Redirigir a la URL de eliminación si el usuario confirma
//                         window.location.href = deleteUrl;
//                     }
//                 });
//             });
//         });
//     };
// });

document.addEventListener('DOMContentLoaded', function() {

    // Función de confirmación para SweetAlert
    function confirmAction(title, text, confirmText, cancelText, formId) {
        Swal.fire({
            title: title,
            text: text,
            icon: "question",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: confirmText,
            cancelButtonText: cancelText
        }).then((result) => {
            if (result.isConfirmed) {                           
                document.getElementById(formId).submit();                
            }
        });
    }

    // Comprobamos la clase en el body para identificar la página actual
    if (document.body.classList.contains('task-update-page')) {
        document.getElementById('confirmUpdateBtn').addEventListener('click', function(e) {
            e.preventDefault();
            confirmAction("Actualizar Tarea", "¿Estás seguro de que deseas actualizar esta tarea?", "Sí, actualizar", "Cancelar", 'taskUpdateForm');
        });
    }

    if (document.body.classList.contains('task-create-page')) {
        document.getElementById('confirmCreateBtn').addEventListener('click', function(e) {
            e.preventDefault();
            confirmAction("Agregar Tarea", "¿Estás seguro de que deseas agregar esta tarea?", "Sí, agregar", "Cancelar", 'taskCreateForm');
        });
    }

    if (document.body.classList.contains('task-list-page') || document.body.classList.contains('task-detail-page')) {
        const deleteButtons = document.querySelectorAll('.deleteTaskBtn');
        
        deleteButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                
                const deleteUrl = this.getAttribute('data-url');
                
                Swal.fire({
                    title: "Eliminar Tarea",
                    text: "¿Estás seguro de que deseas eliminar esta tarea?",
                    icon: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#d33",
                    cancelButtonColor: "#3085d6",
                    confirmButtonText: "Sí, eliminar",
                    cancelButtonText: "Cancelar"
                }).then((result) => {
                    if (result.isConfirmed) {
                        window.location.href = deleteUrl;
                    }
                });
            });
        });
    }

});
