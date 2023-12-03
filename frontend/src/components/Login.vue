<template>
  <v-container class="login-container" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="login-card" elevation="12">
          <v-avatar class="mx-auto">
            <v-icon dark>mdi-lock-outline</v-icon>
          </v-avatar>
          <v-form @submit.prevent="handleLogin">
            <v-card-title class="text-h5 text-center mt-2 mb-4">
              Sign In
            </v-card-title>
            <v-text-field
              v-model="username"
              label="Username"
              outlined
              required
              :error="error !== ''"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              outlined
              required
              type="password"
              :error="error !== ''"
            ></v-text-field>
            <v-btn type="submit" block color="primary" class="mt-4">
              Sign In
            </v-btn>
            <v-row class="text-center mt-2">
              <v-col>
                <v-progress-circular
                  v-if="isLoading"
                  indeterminate
                  size="20"
                  class="ml-2"
                ></v-progress-circular>
                <span v-if="isLoading" class="ml-2">Signing in...</span>
              </v-col>
            </v-row>
            <v-alert v-if="error !== ''" type="error" class="mt-4">
              {{ error }}
            </v-alert>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import login from '../api/login'; // Import your login function
import { useAppStore } from '@/store/app'

export default {
  setup() {
    const username = ref('');
    const password = ref('');
    const error = ref('');
    const isLoading = ref(false);
    const router = useRouter();

    const handleLogin = async () => {
      error.value = '';
      isLoading.value = true;

      try {
        const response = await login(username.value, password.value);
        const data = await response.json();

        if (response.ok) {
          // Login was successful, set state accordingly
          // You can update your session data here
          error.value = '';
          useAppStore().login();
          router.push('/lookup');
        } else {
          // Login failed, display the error message
          error.value = data.message;
        }
      } catch (error) {
        console.error('An error occurred:', error);
        error.value = 'An error occurred while logging in.';
      } finally {
        isLoading.value = false;
      }
    };

    return { username, password, error, isLoading, handleLogin };
  },
};
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-card {
  padding: 16px;
  text-align: center;
}

</style>
