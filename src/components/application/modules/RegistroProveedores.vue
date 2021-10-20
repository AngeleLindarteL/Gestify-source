<template>
  <h1 class="form-title">Registro Proveedores</h1>
  <form class="global-form-container">
    <div class="register-form">
      <div class="input-container">
        <label for="code" class="input-container__label">Código</label>
        <input
          type="text"
          class="input-container__input"
          name="code"
          id="code"
          required
        />
      </div>
      <div class="input-container">
        <label for="name" class="input-container__label">Nombre</label>
        <input
          type="text"
          class="input-container__input"
          name="name"
          id="name"
          required
        />
      </div>
      <div class="input-container">
        <label for="contactNumber" class="input-container__label"
          >Número de contacto</label
        >
        <input
          type="text"
          class="input-container__input"
          name="contactNumber"
          id="contactNumber"
          required
        />
      </div>
      <div class="input-container">
        <label for="email" class="input-container__label"
          >Correo electrónico</label
        >
        <input
          type="email"
          class="input-container__input"
          name="email"
          id="email"
          required
        />
      </div>
      <div class="input-container">
        <label for="due" class="input-container__label">Saldo pendiente</label>
        <input
          type="number"
          class="input-container__input"
          name="due"
          id="due"
          required
        />
      </div>
      <div class="input-container">
        <label for="product" class="input-container__label">Producto</label>
        <input
          type="text"
          class="input-container__input"
          name="product"
          id="product"
          required
        />
      </div>
    </div>
    <button class="primary-btn primary-btn--margin" type="submit">Registrar proveedor</button>
  </form>
</template>
<script>
export default {
  name: "registroProveedores",
};
</script>