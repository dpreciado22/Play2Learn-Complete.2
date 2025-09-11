import { createRouter, createWebHistory } from 'vue-router'
import AnagramHunt from "./apps/AnagramHunt";
import MathFacts from "./apps/MathFacts";
import Home from './apps/Home.vue'

const routes = [

  { path: '/', name: 'home', component: Home },
  {path: '/anagram-hunt', component: AnagramHunt},
  {path: '/math-facts', component: MathFacts},
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});


export default router;