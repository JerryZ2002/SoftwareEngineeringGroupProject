<template>
  <div class="login-page">
    <div class="form-container">
      <h2><el-text class="mx-1" size="large"></el-text></h2>

      <!-- login form -->
      <el-form v-if="isLoginForm" @submit.prevent="handleLogin" method="post">
        <el-label for="username">用户名:</el-label>
        <input type="text" id="username" v-model="username" required><br/>

        <el-label for="password">密码:</el-label>
        <input type="password" id="password" v-model="password" required><br/>

        <el-button color="#626aef" :dark="isDark" type="primary" @click="handleLogin">登录</el-button>
        <p v-if="errorMessage !== ''" style="color: red;">{{ errorMessage }}</p>
        <p>没有账号？<span @click="toggleForm" class="toggle-link">注册</span></p>
      </el-form>

      <!-- register form -->
      <el-form v-else @submit.prevent="handleRegister" method="post">
        <el-label for="registerUsername">用户名:</el-label>
        <input type="text" id="registerUsername" v-model="registerUsername" required><br/>

        <el-label for="registerPassword">密码:</el-label>
        <input type="password" id="registerPassword" v-model="registerPassword" required><br/>

        <el-label for="confirmPassword">确认密码:</el-label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required><br/>

        <el-button color="#626aef" :dark="isDark" type="primary" @click="handleRegister">注册</el-button>
        <p v-if="errorMessage !== ''" style="color: red;">{{ errorMessage }}</p>
        <p>已有账号？<span @click="toggleForm" class="toggle-link">登录</span></p>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoginForm: true, 
      username: '', 
      password: '', 
      registerUsername: '', 
      registerPassword: '',
      confirmPassword: '',
      errorMessage: '',
      isDark: false,
      isLoggedIn: false
    }
  },
  methods: {
    toggleForm() {
      this.isLoginForm = !this.isLoginForm;
      this.clearInputs();
    },
    handleLogin() {
      const savedUser = JSON.parse(localStorage.getItem(this.username));
      if (savedUser && savedUser.password === this.password) {
        this.isLoggedIn = true;
        this.$router.push({ name: 'home' });
        console.log('Login successful!');
      } else {
        this.errorMessage = "用户名或密码不正确";
      }
    },
    handleRegister() {
      if (this.registerPassword !== this.confirmPassword) {
        this.errorMessage = "密码不匹配";
        return;
      }
      const newUser = {
        username: this.registerUsername,
        password: this.registerPassword
      };
      localStorage.setItem(this.registerUsername, JSON.stringify(newUser));
      console.log('Register successful with username:', this.registerUsername);
      // When registration is successful, automatically log in
      this.clearInputs();
      this.isLoginForm = true;
    },
    clearInputs() {
      this.username = '';
      this.password = '';
      this.registerUsername = '';
      this.registerPassword = '';
      this.confirmPassword = '';
      this.errorMessage = '';
    }
  }
}
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
}

.login-page {
  background-image: url(' /src/pic/R.jpeg');
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}

.form-container {
  position: relative;
  width: 10%;
  min-width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
}

h2 {
  text-align: center;
}

label {
  display: block;
  font-weight: bold;
}

input[type=text], input[type=password] {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 8px;
  cursor: pointer;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.toggle-link {
  color: blue;
  cursor: pointer;
  text-decoration: underline;
}
</style>
