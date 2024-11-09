$(document).ready(function(){

    if(document.body.classList.contains('task-update-page')) {
        document.getElementById('confirmUpdateBtn').addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                title: "Actualizar Tarea",
                text: "¿Estás seguro de que deseas actualizar esta tarea?",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Sí, actualizar",
                cancelButtonText: "Cancelar"
            }).then((result) => {
                if (result.isConfirmed) {                           
                    document.getElementById('taskUpdateForm').submit();                
                }
            });            
        });
    };

    if(document.body.classList.contains('task-create-page')) {
        document.getElementById('confirmCreateBtn').addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                title: "Agregar Tarea",
                text: "¿Estás seguro de que deseas agregar esta tarea?",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Sí, agregar",
                cancelButtonText: "Cancelar"
            }).then((result) => {
                if (result.isConfirmed) {                           
                    document.getElementById('taskCreateForm').submit();                
                }
            });
        });
    };

    
});