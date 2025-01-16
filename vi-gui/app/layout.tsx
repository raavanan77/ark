"use client";

//import type { Metadata } from "next";import { useToast } from "@/hooks/use-toast"
import {
  Toast,
  ToastClose,
  ToastDescription,
  ToastProvider,
  ToastTitle,
  ToastViewport,
} from "@/components/ui/toast"
import localFont from "next/font/local";
import "./globals.css";
import { ThemeProvider } from "@/components/theme-provider"
import { useState } from "react";
import { useRouter } from "next/navigation";
import { AppSidebar } from "@/components/app-sidebar";
import { SidebarInset, SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { useToast } from "@/hooks/use-toast";
import { NavigationMenuDemo } from "@/components/nav-menu";
import { ThemeToggle } from "@/components/darmode-toogle";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});
if (geistSans&& geistMono) {
  console.log('Active component');
}

//export const metadata: Metadata = {
//  title: "Vi",
//  description: "Built with sadness",
//};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [isLogin, setLogin] = useState<boolean>();
  const [activeComponent, setActiveComponent] = useState<string | null>(null);
  const router = useRouter(); // Access router
  if (activeComponent) {
    console.log('Active component:', activeComponent);
}
  const handleNavItemClick = (title: string) => {
    console.log(title)
    setActiveComponent(title); // Update the active component
    // Navigate to corresponding route based on the sidebar item clicked
    switch (title) {
      case "Testcase":
        router.push("/testcases");
        break;
      case "Testcase Builder":
          router.push("/testcaseBuilder");
          break;
      case "Device List":
        router.push("/devices/add");
        break;
        case "DUT Profiles":
          router.push("/devices/dutprofiles");
          break;
      case "Documentation":
        router.push("/documentation");
        break;
      case "Settings":
        router.push("/settings");
        break;
      default:
        router.push("/");
    }
  };

  const { toasts } = useToast()
  return (
    
    <html lang="en">
      <body
      >
      <ThemeProvider
      attribute="class"
      defaultTheme="light"
      enableSystem
      disableTransitionOnChange
      >
      <SidebarProvider>
        <AppSidebar onNavItemClick={handleNavItemClick}/>
        <SidebarInset>
        <header className="flex h-12 shrink-0 items-center gap-2 border-b">
          <div className="flex items-center gap-2 px-3">
            <SidebarTrigger/>
            <NavigationMenuDemo/>
            <ThemeToggle/>
          </div>
        </header>
          <div className="flex flex-1 flex-col gap-4 p-4 pt-0">
            <div className="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min">
              {children}
            </div>
          </div>
        </SidebarInset>
      </SidebarProvider>
      <ToastProvider>
      {toasts.map(function ({ id, title, description, action, ...props }) {
        return (
          <Toast key={id} {...props}>
            <div className="grid gap-1">
              {title && <ToastTitle>{title}</ToastTitle>}
              {description && (
                <ToastDescription>{description}</ToastDescription>
              )}
            </div>
            {action}
            <ToastClose />
          </Toast>
        )
      })}
      <ToastViewport />
    </ToastProvider>
      </ThemeProvider>
      </body>
    </html>
  );
}
