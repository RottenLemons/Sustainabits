
<script setup lang="ts">
  import { RouterLink, RouterView, useRouter } from 'vue-router'
  import Menubar from 'primevue/menubar';
  import Badge from 'primevue/badge';
  import Button from 'primevue/button';
  import { ref } from "vue";
  import { useCookies } from '@vueuse/integrations/useCookies'

  const cookies = useCookies()
  const router = useRouter();
  const items = ref([
      {
          label: 'Competitions',
          icon: 'pi pi-gift',
          url: '/competitions'
      },
      {
          label: 'Events',
          icon: 'pi pi-calendar-plus',
          url: '/events'
      },
      {
          label: 'Activities',
          icon: 'pi pi-map',
          url: '/activities'
      },
      {
          label: 'Users',
          icon: 'pi pi-users',
          url: '/users'
      },
      {
          label: 'Trees',
          icon: 'pi pi-star',
          url: '/trees'
      },
  ]);
  const user = ref(cookies.get('user'));

  cookies.addChangeListener((event) => {
    user.value = event.value;
  })

  const logout = () => {
    cookies.remove('user');
    router.push('/login');
  }
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
            <RouterLink v-if="user" style="text-decoration: none; color: inherit;" :to="item.url!">
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
                <RouterLink v-if="!user" style="text-decoration: none;" to="/login">
                  <Button outlined>Login</Button>
                </RouterLink>    
                
                <RouterLink v-if="user" style="text-decoration: none;" to="/profile">
                  <Button text rounded icon="pi pi-user"></Button>
                </RouterLink>  

                
                <Button v-if="user" text rounded icon="pi pi-sign-out" @click="logout"></Button>
                
              </div>
          </template>
      </Menubar>
  </div>

  <RouterView />

  <div class="flex align-items-center justify-content-center" style="backgroundColor: #344e41; width: 100%; height: 150px;">
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

  .p-menubar {
    border-radius: 0px;
  }

</style>
