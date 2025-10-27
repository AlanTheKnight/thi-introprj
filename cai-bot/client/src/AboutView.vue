<template>
  <div class="mt-5 px-5">
    <h1 class="text-3xl font-bold text-center mb-5">About</h1>

    <Card>
      <CardHeader>
        <CardTitle class="text-2xl font-semibold">Our Team</CardTitle>
      </CardHeader>
      <CardContent>
        <CardDescription class="mb-4">
          We are a dedicated team of developers passionate about creating innovative AI solutions.
        </CardDescription>
        <ul class="list-disc list-inside space-y-2">
          <li><strong>John Doe</strong></li>
          <li><strong>Jane Smith</strong></li>
          <li><strong>Bob Johnson</strong></li>
          <li><strong>Alice Davis</strong></li>
        </ul>
      </CardContent>
    </Card>
  </div>
</template>

<script lang="ts" setup>
import { CardHeader, CardTitle, CardDescription, CardContent, Card } from './components/ui/card'
</script>

<style></style>
