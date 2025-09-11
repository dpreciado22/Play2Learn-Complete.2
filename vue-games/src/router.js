import { createRouter, createWebHistory } from 'vue-router'
import AnagramHunt from './apps/AnagramHunt.vue'
import MathFacts from './apps/MathFacts.vue'
import HomeView from './apps/Home.vue'

const routes = [
  { path: '/',               name: 'home',         component: HomeView },
  { path: '/anagram-hunt/',  name: 'anagram-hunt', component: AnagramHunt },
  { path: '/math-facts/',    name: 'math-facts',   component: MathFacts },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() { return { top: 0 } },
})

export default router
