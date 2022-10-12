<template>
    <Hero :brand="customer.brand" :logo="customer.logo" :cta="customer.cta" :slug="customer.slug"
    v-if="foo"
     />
</template>
<script setup lang="ts">
const customer = reactive({
    brand: "FastAPI Github",
    logo: "/images/favicon.gif",
    cta: "⚡ The Best Cloud is no Cloud at all, without giving away your backend",
    slug: "☁️ Deliver value faster with Vipère the Full-Stack Serverless starter kit.",
    
})
const foo = ref(true)

</script>
