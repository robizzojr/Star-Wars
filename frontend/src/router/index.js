import { createRouter, createWebHistory } from 'vue-router'
import Starwars from '../components/Starwars.vue'
import LoginPage from '../components/LoginPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'default',
      redirect: '/login',
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/starwars',
      name: 'starwars',
      component: Starwars,
    },
  ]
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  console.log(authRequired)
  console.log(loggedIn)

  if (authRequired && !loggedIn) {
    return next({ 
      path: '/login', 
      query: { returnUrl: to.path } 
    });
  }

  next();
})

export default router
