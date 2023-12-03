// Composables
import { createRouter, createWebHistory } from 'vue-router'
import { useAppStore } from '@/store/app';

const routes = [
  {
    children: [
      {
        path: '/',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/Home.vue'),
      },
      {
        path: '/login',
        name: 'Login',
        component: () => import('@/components/Login.vue'),
      },
      {
        path: '/lookup',
        name: 'Lookup',
        component: () => import('@/components/LookUp.vue'),
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard specifically for /lookup route
router.beforeEach((to, from, next) => {
  const isAuthenticated = useAppStore().isLoggedIn;

  // Check if the route is /lookup
  if (to.path === '/lookup') {
    // Redirect to login if not authenticated
    if (!isAuthenticated) {
      next('/login'); // Change the path to your login route
      return;
    }
  }

  // Proceed to the route
  next();
});

export default router
