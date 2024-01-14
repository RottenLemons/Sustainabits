
<script setup lang="ts">
  import { RouterLink, RouterView } from 'vue-router'
  // import HelloWorld from './components/HelloWorld.vue'
  import Menubar from 'primevue/menubar';
  import Badge from 'primevue/badge';
  import Button from 'primevue/button';
  import { ref } from "vue";

  const items = ref([
      {
          label: 'Data',
          icon: 'pi pi-database',
          url: '/data'
      },
      {
          label: 'References',
          icon: 'pi pi-link',
          url: '/ref'
      }
  ]);
</script>

<template>
  <div style="background-color: #85B373;">
      <Menubar :model="items">
          <template #start>
            <RouterLink style="text-decoration: none;" to="/">
              <img alt="logo" class="logo" src="@/assets/logo.svg" width="40" height="40" />
            </RouterLink>

          </template>
          <template #item="{ item, props, hasSubmenu, root }">
            <RouterLink style="text-decoration: none; color: inherit;" :to="item.url!">
              <a class="flex align-items-center" v-bind="props.action">
                  <span :class="item.icon" style="color: #3a5a40"/>
                  <span class="ml-2" style="color: #3a5a40">{{ item.label }}</span>
                  <Badge v-if="item.badge" :class="{ 'ml-auto': !root, 'ml-2': root }" :value="item.badge" />
                  <span v-if="item.shortcut" class="ml-auto border-1 surface-border border-round surface-100 text-xs p-1">{{ item.shortcut }}</span>
                  <i v-if="hasSubmenu" :class="['pi pi-angle-down text-primary', { 'pi-angle-down ml-2': root, 'pi-angle-right ml-auto': !root }]"></i>
              </a>
            </RouterLink>
          </template>
          <template #end>
              <div class="flex align-items-center gap-2">
                <!-- <RouterLink style="text-decoration: none;" to="/signup">
                  <Button outlined v-if="!$route.meta.hideLoginSignBtns">SignUp</Button>
                </RouterLink> -->
                <RouterLink style="text-decoration: none;" to="/login">
                  <Button outlined>Login</Button>
                </RouterLink>              
              </div>
          </template>
      </Menubar>
  </div>

  <RouterView />

  <div class="flex align-items-center justify-content-center" style="backgroundColor: #3a5a40; width: 100%; height: 150px;">
        <p style="font-size: large; color: white;">
          Made by Mahir
        </p>
        
    </div>
</template>

<style scoped>

  html {
      font-size: 14px;
  }

  body {
      font-family: var(--font-family);
      font-weight: normal;
      background: var(--surface-ground);
      color: var(--text-color);
      padding: 1rem;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
  }

  p {
      line-height: 1.75;
  } 

</style>
