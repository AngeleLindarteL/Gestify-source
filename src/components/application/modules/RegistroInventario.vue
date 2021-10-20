<template>
  <h1 class="form-title">Registro de inventario</h1>
  <form class="global-form-container">
    <div class="register-form">
      <div class="input-container">
        <label for="product" class="input-container__label">Producto</label>
        <select
          class="input-container__input"
          name="product"
          id="product"
          required
        >
          <option value="0">Seleccione</option>
          <option value="1">Arroz</option>
          <option value="2">Aceite</option>
        </select>
      </div>
      <div class="input-container">
        <label for="quantity" class="input-container__label">Cantidad</label>
        <div class="double-input">
          <input
            type="number"
            class="input-container__input"
            name="quantity"
            id="quantity"
            required
          />
          <select class="input-container__input" name="unit" id="unit" required>
            <option value="0">Seleccione</option>
            <option value="1">Kilos</option>
            <option value="2">Libras</option>
          </select>
        </div>
      </div>
      <div class="input-container">
        <label for="unitPrice" class="input-container__label"
          >Costo unitario</label
        >
        <input
          type="number"
          class="input-container__input"
          name="unitPrice"
          id="unitPrice"
          required
        />
      </div>
      <div class="input-container">
        <label for="expirationDate" class="input-container__label"
          >Fecha vencimiento</label
        >
        <input
          type="date"
          class="input-container__input"
          name="expirationDate"
          id="expirationDate"
          required
        />
      </div>
    </div>
    <button class="primary-btn primary-btn--margin" type="submit">
      Ingresar producto a inventario
    </button>
  </form>
</template>
<script>
export default {
  name: "registroInventario",
};
</script>