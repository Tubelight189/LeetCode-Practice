#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *create (int value){
        struct node*p=(struct node*)malloc(sizeof(struct node));
        p->data=value;p->next=NULL;
        return p;
}
void trv(struct node *head)
{
    struct node *p = head;
    while (p != NULL)
    {
        printf("%d -> ", p->data);
        p = p->next;
    }
}
int count(struct node *head)
{
    int c=0;
    struct node *p = head;
    while (p != NULL){c++;p=p->next;}
    return c;
}
struct node *rev(struct node *head,int left,int right)
{
    if ((left==right))
    {
return head;    }
    
    int c=1;
struct node *p=head;
    while (c<left-1){p = p->next;c++;}
    struct node *lt=p;struct node *r=p;
    printf("...%d",p->data);
    p = p->next;
    struct node *l=p;
    printf("...%d\n",p->data);
    while (c<right){p = p->next;c++;}
    r=p;printf("...%d\n",p->data);
    struct node *prev = NULL;
    struct node *next = NULL;
    p=l;c=left-1;
    while (c<right)
    {
        next = p->next;
        p->next = prev;
        prev = p;
        p = next;c++;
    }
    p = prev;
    lt->next=p;l->next=r;
    // l->next=r->next;
    // r->next=lt;
    // c=0;p=head;
    // p->next=prev;
    return head;
}

void main()
{
    struct node *l1,*l2;
    l1=create(5);
    l1->next=create(2);
    l1->next->next=create(3);
    // l1->next->next->next=create(4);
    // l1->next->next->next->next=create(5);
    // l1->next->next->next->next->next=create(9);
    // l1->next->next->next->next->next->next=create(9);

    // l2=create(9);
    // l2->next=create(9);
    // l2->next->next=create(9);
    // l2->next->next->next=create(9);
    // trv(l1);printf("\n");
    // trv(l2);printf("\n");
    struct node*a=rev(l1,2,3);
    trv(a);

}