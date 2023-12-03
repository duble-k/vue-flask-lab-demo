<template>
    <v-toolbar>
      <v-tooltip text="Home" location="bottom">
        <template v-slot:activator="{props}">
          <v-btn v-bind="props" icon to="/">
            <v-icon>
              mdi-home
            </v-icon>
          </v-btn>
        </template>
      </v-tooltip>

      <v-toolbar-title>Lab Demo</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-tooltip text="Lookup" location="bottom">
        <template v-if="isLoggedIn" v-slot:activator="{props}">
          <v-btn v-bind="props" icon to="/lookup">
            <v-icon>
              mdi-magnify
            </v-icon>
          </v-btn>
        </template>
      </v-tooltip>

      <v-tooltip :text="tooltipText" location="bottom">
        <template v-slot:activator="{props}">
          <v-btn v-bind="props" icon to="/login" @click="handleLogInOrOut">
            <v-icon>
              mdi-account
            </v-icon>
          </v-btn>
        </template>
      </v-tooltip>
    </v-toolbar>
</template>

<script>
import { useAppStore } from '@/store/app';
import fetchDeleteCookie from '@/api/fetchDeleteCookie'

export default {
  methods: {
    async handleLogInOrOut() {
      if(this.isLoggedIn)
      {
        console.log("Logging out");
        await fetchDeleteCookie();
        useAppStore().logout();
      }
    }
  },
  computed: {
    isLoggedIn() {
      return useAppStore().isLoggedIn;
    },
    tooltipText() {
      return this.isLoggedIn ? 'Logout' : 'Login';
    },
  },
};
</script>
