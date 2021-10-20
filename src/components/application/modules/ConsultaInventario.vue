<template>
    <h1>Consulta de inventario</h1>
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
                <th>Stock</th>
                <th>Fecha ingreso</th>
                <th>Proveedor</th>
                <th>Categoría</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ARBLSU-3547</td>
                <td>Arroz Blanco Suelto</td>
                <td>50 Kilos</td>
                <td>30/09/2021</td>
                <td>Arroz Paisa ltda</td>
                <td>Mercado</td>
                <td>íconos</td>
            </tr>
        </tbody>
    </table>
</template>
<script>
export  default {
  name: "consultaInventario",
};
</script>