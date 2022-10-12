import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { createAuth0 } from "@auth0/auth0-vue";
import { setupLayouts } from "virtual:generated-layouts";
import generatedRoutes from "virtual:generated-pages";
import App from "./App.vue";
import "@unocss/reset/tailwind.css";
import "uno.css";
const routes = setupLayouts(generatedRoutes);
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});
const app = createApp(App);
app.use(router);

app.mount("#app");
