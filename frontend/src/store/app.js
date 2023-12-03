// Utilities
import { defineStore } from 'pinia'
import Cookies from 'js-cookie';

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoggedIn: Cookies.get('loggedIn') !== undefined,
  }),
  actions: {
    login() {
      // Update the state and set the "userToken" cookie
      this.isLoggedIn = true;
    },
    logout() {
      // Update the state and remove the "userToken" cookie
      this.isLoggedIn = false;
    },
  },
})
