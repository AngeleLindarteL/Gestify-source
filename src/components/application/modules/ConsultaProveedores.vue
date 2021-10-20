<template>
    <h1>Consulta de proveedores</h1>
    <form action="" class="register-form">
         <div class="input-container">
        <label for="search" class="input-container__label">Buscar</label>
        <input
          type="text"
          class="input-container__input"
          name="search"
          id="search"
          required
        />
        <small>Puedes buscar por código o nombre del producto</small>
      </div>
    </form>
    <table>
        <thead>
            <tr>
                <th>Código</th>
                <th>Nombre</th>
                <th>Contacto</th>
                <th>Correo electrónico</th>
                <th>Saldo</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ARBLSU-3547</td>
                <td>Arroz Paisa ltda</td>
                <td>4465789</td>
                <td>correo@arrozpaisaltda.com</td>
                <td>$0.00</td>
                <td>íconos</td>
            </tr>
        </tbody>
    </table>
</template>
<script>
export  default {
  name: "consultaProveedores",
};
</script>