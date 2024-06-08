import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'


const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: '/',
      name: 'base',
      // component: "../views/Home.vue"
      component: () => import('../App.vue'),
      // meta: { title: 'Home' }, // add meta field
    },
    {
      path: '/Login',
      name: 'Login',
      // component: "../views/Home.vue"
      component: () => import('../Login.vue'),
      // meta: { title: 'Home' }, // add meta field
    },
    {
      path: '/home',
      name: 'home',
      // component: "../views/Home.vue"
      component: () => import('../Home.vue'),
      children:[

        {path:'',component:  () => import('../views/HomeView.vue'),},
        {
          path: '/Products',
          name: 'Products',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('../views/Products.vue')
        },
        {
          path: '/PurchaseOrder',
          name: 'PurchaseOrder',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('../views/PurchaseOrder.vue')
        },
        {
          path: '/Inventories',
          name: 'Inventories',
          component: () => import('../views/Inventories.vue')
        },
        {
          path: '/SalesOrder',
          name: 'SalesOrder',
          component: () => import('../views/SalesOrder.vue')
        },
        {
          path: '/newPages3',
          component: () => import('../views/newPage3.vue')
        },

      ]
    },
  ]
})

export default router

router.beforeEach((to, from, next) => {
  /* change document title when router changes */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})