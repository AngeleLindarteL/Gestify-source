<template>
  <div class="center-content-column">
    <div class="login-form-container">
      <div class="bg-login"></div>
      <div class="white-container">
        <form class="login-form">
          <h1 class="form-title">Inicio de sesión</h1>
          <div class="input-container">
            <label for="email" class="input-container__label"
              >Correo electrónico</label
            >
            <input
              type="email"
              class="input-container__input"
              name="email"
              id="email"
            />
          </div>
          <div class="input-container">
            <label for="password" class="input-container__label"
              >Contraseña</label
            >
            <input
              type="password"
              class="input-container__input"
              name="password"
              id="pass"
            />
          </div>
          <button type="submit" class="primary-btn">Iniciar sesión</button>
        </form>
        <div class="bottom-actions">
          <p>
            <a href="#" class="bottom-actions__link"
              >¿Olvidaste la contraseña?</a
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "logIn",
};
</script>
